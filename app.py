from fastapi import FastAPI, HTTPException,Depends
from sqlalchemy.exc import IntegrityError
from controllers import Controllers
from models import User,HealthRecord
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_db
from schemas import UserCreate,UserResponse,CaloriesResponse,CaloriesRequest
from security import hash_password, verify_password





app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/db_health")
def db_health(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database connection error")


@app.post("/register_user",response_model=UserResponse, status_code=201)
def register_user(request:UserCreate, db:Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == request.email.lower()).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    create_user = User(
        name= request.name,
        nickname = request.nickname,
        email = request.email.lower(),
        password_hash = hash_password(request.password)
    )
    db.add(create_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already registered")
    except Exception:
        db.rollback()
        raise HTTPException(status_code=500, detail="Error creating user")

    db.refresh(create_user)
    return create_user


@app.post("/calculate_calories",response_model=CaloriesResponse, status_code=200)
def get_calories(request:CaloriesRequest,db:Session = Depends(get_db)):
    try:
        bmi = Controllers.calculate_bmi(request.weight,request.height)
        bmr = Controllers.calculate_bmr(request.weight,request.height,request.age,request.sex)
        category = Controllers.judge_bmi(bmi)
        activity_number = Controllers.record_activityType(request.activity)
        calories = Controllers.calculate_calories(bmr,request.goal.value,activity_number)

        health_record = HealthRecord(
            weight_kg=request.weight,
            height_m=request.height,
            age=request.age,
            sex=request.sex,
            goal=request.goal,
            activity=request.activity,
            bmi=bmi,
            bmr=bmr,
            calories=calories,
            category=category
        )
        db.add(health_record)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise HTTPException(status_code=400, detail="Error saving health record")
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return health_record
   