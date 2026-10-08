def calculate_bmi(weight, height):
    """Calculates BMI given weight in kg and height in cm."""
    if not height or not weight or height <= 0:
        return 0.0
    height_m = height / 100.0
    return round(weight / (height_m ** 2), 2)

def assign_workout_plan(weight):
    """
    Smart Assignment: Assign workout plans based on 10kg weight classes 
    (ranging from 50kg to 120kg).
    """
    if weight is None:
        return "No Plan Assigned"
        
    w = float(weight)
    
    if w < 50:
        return "Underweight Foundation Plan"
    elif 50 <= w < 60:
        return "Beginner Hypertrophy - Class 50-60kg"
    elif 60 <= w < 70:
        return "Lean Muscle Builder - Class 60-70kg"
    elif 70 <= w < 80:
        return "Athletic Conditioning - Class 70-80kg"
    elif 80 <= w < 90:
        return "Strength & Power Focus - Class 80-90kg"
    elif 90 <= w < 100:
        return "Heavy Lifter Routine - Class 90-100kg"
    elif 100 <= w < 110:
        return "Mass & Mobility - Class 100-110kg"
    elif 110 <= w < 120:
        return "Advanced Strength - Class 110-120kg"
    else:
        return "Super-Heavyweight Custom Plan"
