def generate_diet_plan(bmi, goal):
    if bmi > 30:
        goal_applied = "Calorie Deficit"
    elif goal == "Muscle Gain":
        goal_applied = "High Protein/Surplus"
    else:
        goal_applied = "Balanced Maintenance"
        
    if goal_applied == "Calorie Deficit":
        return {
            "breakfast": "Egg white omelet with spinach and tomatoes",
            "lunch": "Grilled turkey breast salad with olive oil dressing",
            "dinner": "White fish, quinoa, and green beans",
            "snacks": "Protein shake and an apple"
        }
    elif goal_applied == "High Protein/Surplus":
        return {
            "breakfast": "Oatmeal with whey protein, peanut butter, and banana",
            "lunch": "Chicken breast, brown rice, and broccoli",
            "dinner": "Salmon, sweet potato, and asparagus",
            "snacks": "Greek yogurt with almonds and honey"
        }
    else:
        return {
            "breakfast": "Whole wheat toast with avocado and poached eggs",
            "lunch": "Tuna salad wrap with whole grain tortilla",
            "dinner": "Lean beef stir-fry with mixed vegetables",
            "snacks": "Cottage cheese and mixed berries"
        }
