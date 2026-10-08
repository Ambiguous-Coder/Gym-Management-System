from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
db = client['GymManagementDB']
plans_coll = db['plans']

# Clear existing plans to ensure fresh 10 curriculums
plans_coll.delete_many({"type": "workout"})

WORKOUT_CURRICULUMS = [
    {
        "name": "Underweight Foundation Plan",
        "details": {
            "range": "Under 50kg",
            "badge": "< 50kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Chest & Triceps", "exercises": ["Push-ups (Assisted)", "Machine Press", "Tricep Dips (Bench)"]},
                "Tuesday": {"focus": "Back & Biceps", "exercises": ["Lat Pulldowns", "Seated Rows", "Dumbbell Curls"]},
                "Wednesday": {"focus": "Legs & Abs", "exercises": ["Bodyweight Squats", "Leg Extensions", "Plank"]},
                "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Dumbbell Shoulder Press", "Lateral Raises", "Shrugs"]},
                "Friday": {"focus": "Full Body / Compound", "exercises": ["Goblet Squats", "Dumbbell Deadlifts"]},
                "Saturday": {"focus": "Cardio & Core", "exercises": ["Light Walking: 20 Mins", "Crunches"]},
                "Sunday": {"focus": "Rest Day", "exercises": ["Recovery & Stretching"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Beginner Hypertrophy - Class 50-60kg",
        "details": {
            "range": "50-60kg",
            "badge": "50-60kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Chest & Triceps", "exercises": ["Incline DB Press", "Flat Bench Press", "Tricep Pushdowns"]},
                "Tuesday": {"focus": "Back & Biceps", "exercises": ["Seated Cable Rows", "Pull-ups (Assisted)", "Hammer Curls"]},
                "Wednesday": {"focus": "Legs & Abs", "exercises": ["Leg Press", "Walking Lunges", "Russian Twists"]},
                "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Overhead Barbell Press", "Front Raises", "Shrugs"]},
                "Friday": {"focus": "Full Body", "exercises": ["Deadlifts (Light)", "Push-ups"]},
                "Saturday": {"focus": "Cardio", "exercises": ["Stationary Bike: 20 Mins", "Leg Raises"]},
                "Sunday": {"focus": "Rest Day", "exercises": ["Complete Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Lean Muscle Builder - Class 60-70kg",
        "details": {
            "range": "60-70kg",
            "badge": "60-70kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Upper Body", "exercises": ["Bench Press", "Rows", "Shoulder Press"]},
                "Tuesday": {"focus": "Lower Body", "exercises": ["Squats", "Leg Curls", "Calf Raises"]},
                "Wednesday": {"focus": "Rest", "exercises": ["Stretching"]},
                "Thursday": {"focus": "Upper Body", "exercises": ["Incline Press", "Lat Pulldown", "Curls"]},
                "Friday": {"focus": "Lower Body", "exercises": ["Deadlifts", "Lunges", "Abs"]},
                "Saturday": {"focus": "Active Recovery", "exercises": ["Light Jog"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Athletic Conditioning - Class 70-80kg",
        "details": {
            "range": "70-80kg",
            "badge": "70-80kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Strength", "exercises": ["Deadlifts", "Pull-ups", "Dips"]},
                "Tuesday": {"focus": "Conditioning", "exercises": ["Kettlebell Swings", "Burpees", "Sprints"]},
                "Wednesday": {"focus": "Recovery", "exercises": ["Yoga"]},
                "Thursday": {"focus": "Strength", "exercises": ["Squats", "Overhead Press", "Rows"]},
                "Friday": {"focus": "Conditioning", "exercises": ["Box Jumps", "Wall Balls", "Rope Climbs"]},
                "Saturday": {"focus": "Endurance", "exercises": ["5km Run"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Strength & Power Focus - Class 80-90kg",
        "details": {
            "range": "80-90kg",
            "badge": "80-90kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Max Strength", "exercises": ["Squats", "Bench Press", "Rows"]},
                "Tuesday": {"focus": "Rest", "exercises": ["Rest"]},
                "Wednesday": {"focus": "Explosive Power", "exercises": ["Power Cleans", "Box Jumps", "Sprints"]},
                "Thursday": {"focus": "Rest", "exercises": ["Rest"]},
                "Friday": {"focus": "Max Strength", "exercises": ["Deadlifts", "Overhead Press", "Pull-ups"]},
                "Saturday": {"focus": "Active Recovery", "exercises": ["Swimming"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Heavy Lifter Routine - Class 90-100kg",
        "details": {
            "range": "90-100kg",
            "badge": "90-100kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Chest", "exercises": ["Incline Bench", "Cable Flyes", "Push-ups"]},
                "Tuesday": {"focus": "Back", "exercises": ["Deadlifts", "T-Bar Rows", "Pull-ups"]},
                "Wednesday": {"focus": "Legs", "exercises": ["Squats", "Leg Press", "Calf Raises"]},
                "Thursday": {"focus": "Shoulders", "exercises": ["Military Press", "Lateral Raises", "Face Pulls"]},
                "Friday": {"focus": "Arms", "exercises": ["Barbell Curls", "Skull Crushers", "Hammer Curls"]},
                "Saturday": {"focus": "Cardio", "exercises": ["Walking"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Mass & Mobility - Class 100-110kg",
        "details": {
            "range": "100-110kg",
            "badge": "100-110kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Full Body", "exercises": ["Clean & Press", "Squats", "Rows"]},
                "Tuesday": {"focus": "Mobility", "exercises": ["Dynamic Stretching", "Foam Rolling"]},
                "Wednesday": {"focus": "Full Body", "exercises": ["Deadlifts", "Bench Press", "Pull-ups"]},
                "Thursday": {"focus": "Mobility", "exercises": ["Yoga", "Core Stability"]},
                "Friday": {"focus": "Full Body", "exercises": ["Lunges", "Shoulder Press", "Dips"]},
                "Saturday": {"focus": "Active Recovery", "exercises": ["Walking"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Advanced Strength - Class 110-120kg",
        "details": {
            "range": "110-120kg",
            "badge": "110-120kg",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Squat Focus", "exercises": ["Back Squats", "Pause Squats", "Leg Extensions"]},
                "Tuesday": {"focus": "Bench Focus", "exercises": ["Bench Press", "Spoto Press", "Tricep Dips"]},
                "Wednesday": {"focus": "Rest", "exercises": ["Rest"]},
                "Thursday": {"focus": "Deadlift Focus", "exercises": ["Deadlifts", "Deficit Deadlifts", "Rows"]},
                "Friday": {"focus": "Accessory Work", "exercises": ["Overhead Press", "Pull-ups", "Abs"]},
                "Saturday": {"focus": "Conditioning", "exercises": ["Sled Pushes"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Super-Heavyweight Custom Plan",
        "details": {
            "range": "120kg+",
            "badge": "120kg+",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "Maintenance", "exercises": ["Machine Press", "Seated Rows"]},
                "Tuesday": {"focus": "Mobility", "exercises": ["Walking", "Light Stretching"]},
                "Wednesday": {"focus": "Maintenance", "exercises": ["Leg Press", "Lat Pulldown"]},
                "Thursday": {"focus": "Rest", "exercises": ["Rest"]},
                "Friday": {"focus": "Maintenance", "exercises": ["Shoulder Machine", "Curls"]},
                "Saturday": {"focus": "Walking", "exercises": ["30 Mins Walk"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    },
    {
        "name": "Fat Loss Specialist",
        "details": {
            "range": "Any Weight",
            "badge": "Fat Loss",
            "sets_reps": "3 sets of 12 reps",
            "schedule": {
                "Monday": {"focus": "HIIT", "exercises": ["Burpees", "Mountain Climbers", "Jumping Jacks"]},
                "Tuesday": {"focus": "Strength", "exercises": ["Squats", "Push-ups", "Lunges"]},
                "Wednesday": {"focus": "Cardio", "exercises": ["30 Mins Run"]},
                "Thursday": {"focus": "HIIT", "exercises": ["Plank", "Box Jumps", "Rope Waves"]},
                "Friday": {"focus": "Strength", "exercises": ["Deadlifts", "Shoulder Press", "Rows"]},
                "Saturday": {"focus": "Active Recovery", "exercises": ["Biking"]},
                "Sunday": {"focus": "Rest", "exercises": ["Rest"]}
            }
        },
        "type": "workout"
    }
]

plans_coll.insert_many(WORKOUT_CURRICULUMS)
print("Successfully populated 10 workout curriculums.")
