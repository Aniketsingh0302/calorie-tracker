from enum import Enum

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