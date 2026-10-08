# data_manager.py

WORKOUT_CLASSES = {
    "Underweight Foundation Plan": {
        "range": "Under 50kg",
        "badge": "< 50kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Push-ups (Assisted): 3 Sets x 10 Reps", "Machine Press: 3 Sets x 12 Reps", "Tricep Dips (Bench): 3 Sets x 10 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Lat Pulldowns: 3 Sets x 12 Reps", "Seated Rows: 3 Sets x 10 Reps", "Dumbbell Curls: 3 Sets x 12 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Bodyweight Squats: 3 Sets x 15 Reps", "Leg Extensions: 3 Sets x 12 Reps", "Plank: 3 Sets x 30 Secs"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Dumbbell Shoulder Press: 3 Sets x 10 Reps", "Lateral Raises: 3 Sets x 12 Reps", "Shrugs: 3 Sets x 12 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Goblet Squats: 3 Sets x 12 Reps", "Dumbbell Deadlifts: 3 Sets x 10 Reps"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Light Walking: 20 Mins", "Crunches: 3 Sets x 15 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Recovery & Stretching"]}
        }
    },
    "Beginner Hypertrophy - Class 50-60kg": {
        "range": "50-60kg",
        "badge": "50-60kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Incline Dumbbell Press: 3 Sets x 12 Reps", "Flat Bench Press: 3 Sets x 10 Reps", "Tricep Pushdowns: 3 Sets x 12 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Seated Cable Rows: 3 Sets x 12 Reps", "Pull-ups (Assisted): 3 Sets x 8 Reps", "Hammer Curls: 3 Sets x 12 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Leg Press: 3 Sets x 12 Reps", "Walking Lunges: 3 Sets x 12 Reps", "Russian Twists: 3 Sets x 15 Reps"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Overhead Barbell Press: 3 Sets x 10 Reps", "Front Raises: 3 Sets x 12 Reps", "Shrugs: 3 Sets x 12 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Deadlifts (Light): 3 Sets x 8 Reps", "Push-ups: 3 Sets x 15 Reps"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Stationary Bike: 20 Mins", "Hanging Leg Raises: 3 Sets x 12 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Complete Rest"]}
        }
    },
    "Lean Muscle Builder - Class 60-70kg": {
        "range": "60-70kg",
        "badge": "60-70kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Barbell Bench Press: 4 Sets x 10 Reps", "Incline Flyes: 3 Sets x 12 Reps", "Skull Crushers: 3 Sets x 10 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Barbell Rows: 4 Sets x 10 Reps", "Lat Pulldown: 3 Sets x 12 Reps", "Preacher Curls: 3 Sets x 10 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Back Squats: 4 Sets x 10 Reps", "Romanian Deadlifts: 3 Sets x 12 Reps", "Cable Crunches: 3 Sets x 15 Reps"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Military Press: 4 Sets x 10 Reps", "Lateral Raises: 4 Sets x 12 Reps", "Upright Rows: 3 Sets x 10 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Clean & Press: 3 Sets x 8 Reps", "Pull-ups: 3 Sets x Max Reps"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["HIIT Treadmill: 15 Mins", "Plank: 3 Sets x 45 Secs"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Complete Rest"]}
        }
    },
    "Athletic Conditioning - Class 70-80kg": {
        "range": "70-80kg",
        "badge": "70-80kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Heavy Barbell Press: 4 Sets x 8 Reps", "Weighted Dips: 3 Sets x 10 Reps", "Overhead Tricep Ext: 3 Sets x 12 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Weighted Pull-ups: 4 Sets x 8 Reps", "T-Bar Rows: 3 Sets x 10 Reps", "Barbell Curls: 3 Sets x 10 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Front Squats: 4 Sets x 8 Reps", "Leg Press: 3 Sets x 12 Reps", "Hanging Leg Raises: 4 Sets x 12 Reps"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Arnold Press: 4 Sets x 10 Reps", "Face Pulls: 3 Sets x 15 Reps", "Heavy Shrugs: 4 Sets x 12 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Deadlifts: 4 Sets x 6 Reps", "Farmer's Walk: 3 Sets x 30m"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Rowing Machine: 20 Mins", "Ab Wheel Rollouts: 3 Sets x 15 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Complete Rest"]}
        }
    },
    "Strength & Power Focus - Class 80-90kg": {
        "range": "80-90kg",
        "badge": "80-90kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Bench Press (Heavy): 5 Sets x 5 Reps", "Incline Dumbbell Press: 3 Sets x 8 Reps", "Close-Grip Bench: 3 Sets x 8 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Pendlay Rows: 5 Sets x 5 Reps", "Weighted Chin-ups: 3 Sets x 8 Reps", "Heavy Hammer Curls: 3 Sets x 8 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Heavy Back Squats: 5 Sets x 5 Reps", "Hack Squats: 3 Sets x 8 Reps", "Weighted Crunches: 3 Sets x 15 Reps"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Standing Overhead Press: 5 Sets x 5 Reps", "Lateral Raises: 4 Sets x 12 Reps", "Barbell Shrugs: 4 Sets x 10 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Power Cleans: 5 Sets x 3 Reps", "Push Press: 3 Sets x 5 Reps"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Stair Climber: 20 Mins", "Cable Woodchoppers: 3 Sets x 12 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Complete Rest"]}
        }
    },
    "Heavy Lifter Routine - Class 90-100kg": {
        "range": "90-100kg",
        "badge": "90-100kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Bench Press (Heavy): 5 Sets x 3-5 Reps", "Weighted Dips: 4 Sets x 8 Reps", "French Press: 3 Sets x 10 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Deadlifts (Standard): 5 Sets x 3-5 Reps", "Yates Rows: 4 Sets x 8 Reps", "Preacher Curls: 3 Sets x 10 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Squats (Heavy): 5 Sets x 3-5 Reps", "Leg Press (Heavy): 4 Sets x 8 Reps", "Weighted Planks: 3 Sets x 60 Secs"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Seated Overhead Press: 5 Sets x 5 Reps", "Reverse Pec Deck: 3 Sets x 12 Reps", "Heavy Dumbbell Shrugs: 4 Sets x 12 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Snatch Grip Deadlifts: 3 Sets x 5 Reps", "Incline Bench Press: 3 Sets x 8 Reps"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Assault Bike: 15 Mins", "Hanging Leg Raises: 3 Sets x 15 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Complete Rest"]}
        }
    },
    "Mass & Mobility - Class 100-110kg": {
        "range": "100-110kg",
        "badge": "100-110kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Incline Barbell Press: 4 Sets x 8 Reps", "Flat Dumbbell Press: 4 Sets x 8 Reps", "Tricep Pushdowns: 4 Sets x 10 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Chest-Supported Rows: 4 Sets x 8 Reps", "Lat Pulldown: 4 Sets x 10 Reps", "Concentration Curls: 3 Sets x 10 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Box Squats: 4 Sets x 8 Reps", "Bulgarian Split Squats: 3 Sets x 10 Reps", "Ab Wheel: 3 Sets x 12 Reps"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Smith Machine Press: 4 Sets x 8 Reps", "Lateral Raises: 4 Sets x 12 Reps", "Upright Rows: 3 Sets x 10 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Trap Bar Deadlifts: 4 Sets x 6 Reps", "Farmer's Carry: 3 Sets x 40m"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Low-Impact Elliptical: 25 Mins", "Russian Twists: 3 Sets x 20 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Mobility Work & Rest"]}
        }
    },
    "Advanced Strength - Class 110-120kg": {
        "range": "110-120kg",
        "badge": "110-120kg",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Heavy Flat Bench: 5 Sets x 5 Reps", "Spoto Press: 3 Sets x 6 Reps", "Skull Crushers: 4 Sets x 8 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Block Pulls: 5 Sets x 5 Reps", "Meadows Rows: 3 Sets x 8 Reps", "Heavy Barbell Curls: 4 Sets x 8 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Pause Squats: 5 Sets x 5 Reps", "Heavy Leg Extensions: 3 Sets x 10 Reps", "Cable Crunches: 4 Sets x 12 Reps"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Heavy Push Press: 5 Sets x 5 Reps", "Rear Delt Flyes: 4 Sets x 12 Reps", "Power Shrugs: 5 Sets x 8 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Deficit Deadlifts: 3 Sets x 5 Reps", "Floor Press: 3 Sets x 6 Reps"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Swimming/Rowing: 20 Mins", "Hanging Leg Raises: 4 Sets x 15 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Active Recovery"]}
        }
    },
    "Super-Heavyweight Custom Plan": {
        "range": "120kg+",
        "badge": "120kg+",
        "schedule": {
            "Monday": {"focus": "Chest & Triceps", "exercises": ["Machine Chest Press: 4 Sets x 10 Reps", "Pec Deck: 3 Sets x 12 Reps", "Rope Pushdowns: 3 Sets x 15 Reps"]},
            "Tuesday": {"focus": "Back & Biceps", "exercises": ["Lat Pulldown: 4 Sets x 10 Reps", "Seated Cable Row: 3 Sets x 12 Reps", "Machine Curls: 3 Sets x 12 Reps"]},
            "Wednesday": {"focus": "Legs & Abs", "exercises": ["Leg Press: 4 Sets x 12 Reps", "Lying Leg Curls: 3 Sets x 12 Reps", "Plank: 3 Sets x 45 Secs"]},
            "Thursday": {"focus": "Shoulders & Traps", "exercises": ["Machine Shoulder Press: 4 Sets x 10 Reps", "Lateral Raises: 3 Sets x 15 Reps", "Shrugs: 3 Sets x 15 Reps"]},
            "Friday": {"focus": "Full Body / Compound Focus", "exercises": ["Goblet Squats: 4 Sets x 10 Reps", "Kettlebell Swings: 3 Sets x 15 Reps"]},
            "Saturday": {"focus": "Cardio & Core", "exercises": ["Stationary Bike/Recumbent: 30 Mins", "Crunches: 3 Sets x 20 Reps"]},
            "Sunday": {"focus": "Rest Day", "exercises": ["Mobility Work & Rest"]}
        }
    }
}
