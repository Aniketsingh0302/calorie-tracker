class Controllers:

    @staticmethod
    def calculate_bmi(weight, height):
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers")
        return weight / (height ** 2)

    @staticmethod
    def judge_bmi(bmi):
        if bmi <= 0:
            raise ValueError("BMI must be positive; check the calculation")
        if bmi < 18.5:
            return "Underweight"
        if bmi < 25:
            return "Normal"
        if bmi < 30:
            return "Overweight"
        return "Obese"

    ACTIVITY_LEVEL = {
        "No Activity":0,
        "Light Activity":1,
        "2-3 days workout":2,
        "Proper Workout(4-6 days)":3

    }

    @staticmethod
    def record_activityType(activity):
        if activity not in Controllers.ACTIVITY_LEVEL:
            raise ValueError(f"Unknown Activity Type:{activity}")
        return Controllers.ACTIVITY_LEVEL[activity]

    @staticmethod
    def calculate_bmr(weight,height,age,sex):
        if weight <= 0 or height <= 0 or age <= 0:
            raise ValueError("Weight, height and age must be positive numbers")
        height_in_cm = height*100
        sex = sex.upper()
        if sex not in("MALE","FEMALE"):
            raise ValueError("Invalid Sex")
        if sex == "MALE":
            return 10*weight+6.25*height_in_cm-5*age+5
        
        return 10*weight+6.25*height_in_cm-5*age-161

    ACTIVITY_MULTIPLIER = {
        0:1.2,
        1:1.375,
        2:1.55,
        3:1.725
    }

    ACTIVITY_GOAL = {
        "BULK":500,
        "CUT":-500,
        "MAINTAIN":0
    }


    @staticmethod
    def calculate_calories(bmr,goal,activity_number):
        if goal not in Controllers.ACTIVITY_GOAL:
            raise ValueError(f"Unknown Goal Type:{goal}")
        if activity_number not in Controllers.ACTIVITY_MULTIPLIER:
            raise ValueError("Unknown Activity Type")
        tdee = bmr*Controllers.ACTIVITY_MULTIPLIER[activity_number]
        return tdee + Controllers.ACTIVITY_GOAL[goal]

a = Controllers.calculate_calories(2000,"CUT",0)
print (a)
    