from fastapi import FastAPI, HTTPException,Depends
from controllers import Controllers
from schemas import  CaloriesRequest
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.orm import Session

from database import get_db





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

@app.post("/calculate_calories")
def get_calories(request:CaloriesRequest):
    try:
        bmi = Controllers.calculate_bmi(request.weight,request.height)
        bmr = Controllers.calculate_bmr(request.weight,request.height,request.age,request.sex)
        category = Controllers.judge_bmi(bmi)
        activity_number = Controllers.record_activityType(request.activity)
        calories = Controllers.calculate_calories(bmr,request.goal.value,activity_number)
        
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {
        "bmi":round(bmi,2),
        "category":category,
        "calories":calories,
        "bmr":round(bmr)
    }