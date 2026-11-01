
from pydantic import BaseModel, Field,ConfigDict,EmailStr
from enums import Sex, ActivityType, Goal

from uuid import UUID


class CaloriesRequest(BaseModel):
    weight: float = Field(gt=0,allow_inf_nan =False, description = "Weight in Kg")
    height: float = Field(gt=0,allow_inf_nan= False, description = "Height in Meters")
    age: int = Field(gt =0, le =120,description = "Age in Years")
    sex: Sex
    activity: ActivityType
    goal: Goal

class CaloriesResponse(BaseModel):
    bmi: float
    category: str
    calories: float
    bmr: float


###Input and output for User creation

class UserCreate(BaseModel):
    name:str = Field(min_length = 2 , max_length = 100, description = "Full Name of the User")
    nickname:str | None = Field(min_length = 2 ,max_length = 50, description = "What should we call you")
    email:EmailStr = Field(description = "Email of the User")
    password:str = Field(min_length = 8, max_length = 100, description = "Password of the User")

class UserResponse(BaseModel):
    id: UUID
    name:str
    nickname:str | None
    email:EmailStr

    model_config = ConfigDict(from_attributes = True)