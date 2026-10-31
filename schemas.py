from enum import Enum
from pydantic import BaseModel, Field


class Sex(str,Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class ActivityType(str,Enum):
    NO_ACTIVITY = "No Activity"
    LIGHT_ACTIVITY = "Light Activity"
    MODERATE_ACTIVITY = "2-3 days workout"
    PROPER_WORKOUT_4_6_DAYS = "Proper Workout(4-6 days)"


class Goal(str,Enum):
    BULK = "BULK"
    CUT = "CUT"
    MAINTAIN = "MAINTAIN"

class CaloriesRequest(BaseModel):
    weight: float = Field(gt=0,allow_inf_nan =False, description = "Weight in Kg")
    height: float = Field(gt=0,allow_inf_nan= False, description = "Height in Meters")
    age: int = Field(gt =0, le =120,description = "Age in Years")
    sex: Sex
    activity: ActivityType
    goal: Goal