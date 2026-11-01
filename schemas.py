
from pydantic import BaseModel, Field
from enums import Sex, ActivityType, Goal

class CaloriesRequest(BaseModel):
    weight: float = Field(gt=0,allow_inf_nan =False, description = "Weight in Kg")
    height: float = Field(gt=0,allow_inf_nan= False, description = "Height in Meters")
    age: int = Field(gt =0, le =120,description = "Age in Years")
    sex: Sex
    activity: ActivityType
    goal: Goal