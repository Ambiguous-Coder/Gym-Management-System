from pymongo import MongoClient
import random
from datetime import datetime

client = MongoClient('mongodb://localhost:27017/')
db = client['GymManagementDB']

# 1. Backup existing members
existing_members = list(db.members.find())
if existing_members:
    db.members_backup.delete_many({})
    db.members_backup.insert_many(existing_members)
    print(f"Backed up {len(existing_members)} members to members_backup.")

# 2. Generate 20 new members
names = ["John Doe", "Jane Smith", "Alex Johnson", "Emily Davis", "Michael Brown", 
         "Sarah Wilson", "David Taylor", "Jessica Miller", "Chris Anderson", "Ashley Thomas",
         "Brian Jackson", "Nicole White", "Kevin Harris", "Amanda Martin", "James Thompson",
         "Megan Garcia", "Robert Martinez", "Stephanie Robinson", "William Clark", "Rachel Lewis"]

genders = ["Male", "Female", "Other"]
goals = ["Muscle Gain", "Weight Loss", "Maintenance"]

new_members = []
for name in names:
    weight = random.uniform(50, 120)
    height = random.uniform(150, 190)
    age = random.randint(18, 60)
    gender = random.choice(genders)
    goal = random.choice(goals)
    
    # Simple logic for plans based on weight
    if weight < 60:
        workout = "Underweight Foundation Plan"
    elif weight < 80:
        workout = "Athletic Conditioning - Class 70-80kg"
    else:
        workout = "Super-Heavyweight Custom Plan"
        
    member = {
        "name": name,
        "phone": f"+1-555-01{random.randint(10, 99)}",
        "email": f"{name.lower().replace(' ', '.')}@example.com",
        "age": age,
        "gender": gender,
        "fitness_goal": goal,
        "metrics": {
            "weight": round(weight, 1),
            "height": round(height, 1),
            "bmi": round(weight / ((height/100)**2), 2)
        },
        "diet_plan": {
            "breakfast": "Oatmeal with fruit",
            "lunch": "Grilled chicken and rice",
            "dinner": "Steamed fish and veggies",
            "snacks": "Protein bar"
        },
        "workout_plan": {
            "routine": workout,
            "sets_reps": "3 sets of 12 reps"
        },
        "attendance": []
    }
    new_members.append(member)

db.members.insert_many(new_members)
print(f"Successfully added 20 new members to the database.")
