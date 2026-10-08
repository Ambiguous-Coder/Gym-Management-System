from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId
from diet_manager import generate_diet_plan
from workout_engine import calculate_bmi, assign_workout_plan
from data_manager import WORKOUT_CLASSES

class DBManager:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['GymManagementDB']
        self.members_coll = self.db['members']
        self.users_coll = self.db['users']
        self.plans_coll = self.db['plans']
        self._init_db()

    def _init_db(self):
        if self.users_coll.count_documents({"username": "admin"}) == 0:
            self.users_coll.insert_one({"username": "admin", "password": "123456", "role": "admin"})
        
        if self.plans_coll.count_documents({}) == 0:
            for name, details in WORKOUT_CLASSES.items():
                self.plans_coll.insert_one({"name": name, "details": details, "type": "workout"})

    def verify_login(self, username, password):
        user = self.users_coll.find_one({"username": username, "password": password})
        return user is not None

    def get_dashboard_stats(self):
        total_members = self.members_coll.count_documents({})
        today = datetime.now().strftime('%Y-%m-%d')
        daily_attendance = self.members_coll.count_documents({"attendance": today})
        health_alerts = self.members_coll.count_documents({"metrics.bmi": {"$gt": 30}})
        return {
            "total_members": total_members,
            "daily_attendance": daily_attendance,
            "health_alerts": health_alerts
        }

    def get_members(self, search_query=None):
        if search_query:
            regex = {"$regex": search_query, "$options": "i"}
            query = {"$or": [{"name": regex}, {"gender": regex}, {"fitness_goal": regex}]}
            members = list(self.members_coll.find(query).sort("_id", -1))
        else:
            members = list(self.members_coll.find().sort("_id", -1))
        for m in members:
            m['id'] = str(m['_id'])
        return members

    def add_member(self, data):
        weight = float(data.get('weight', 0))
        height = float(data.get('height', 0))
        bmi = float(calculate_bmi(weight, height))
        goal = data.get('fitness_goal', 'Maintenance')
        
        diet_plan = generate_diet_plan(bmi, goal)
        template_name = assign_workout_plan(weight)
        
        # Search plans collection for the template (Deep Copy / Cloning Logic)
        template = self.plans_coll.find_one({"name": template_name, "type": "workout"})
        if template:
            personal_workout = template.get('details', {}).get('schedule', {})
        else:
            # Fallback to WORKOUT_CLASSES if not in DB
            personal_workout = WORKOUT_CLASSES.get(template_name, {}).get('schedule', {})
            
        member = {
            "name": data.get('name', ''),
            "phone": data.get('phone', ''),
            "email": data.get('email', ''),
            "age": int(data.get('age', 0) or 0),
            "gender": data.get('gender', ''),
            "fitness_goal": goal,
            "metrics": {
                "weight": weight,
                "height": height,
                "bmi": bmi
            },
            "diet_plan": diet_plan,
            "workout_routine": template_name,
            "personal_workout": personal_workout,
            "attendance": []
        }
        self.members_coll.insert_one(member)
        return True

    def get_member(self, member_id):
        try:
            member = self.members_coll.find_one({"_id": ObjectId(member_id)})
            if member:
                member['id'] = str(member['_id'])
            return member
        except:
            return None

    def update_member(self, member_id, data):
        weight = float(data.get('weight', 0))
        height = float(data.get('height', 0))
        bmi = float(calculate_bmi(weight, height))
        goal = data.get('fitness_goal', 'Maintenance')
        
        diet_plan = generate_diet_plan(bmi, goal)
        template_name = assign_workout_plan(weight)
        
        # Search plans collection for the template (Cloning Logic)
        template = self.plans_coll.find_one({"name": template_name, "type": "workout"})
        if template:
            personal_workout = template.get('details', {}).get('schedule', {})
        else:
            personal_workout = WORKOUT_CLASSES.get(template_name, {}).get('schedule', {})

        update_doc = {
            "$set": {
                "name": data.get('name', ''),
                "phone": data.get('phone', ''),
                "email": data.get('email', ''),
                "age": int(data.get('age', 0) or 0),
                "gender": data.get('gender', ''),
                "fitness_goal": goal,
                "metrics.weight": weight,
                "metrics.height": height,
                "metrics.bmi": bmi,
                "diet_plan": diet_plan,
                "workout_routine": template_name,
                "personal_workout": personal_workout
            }
        }
        try:
            self.members_coll.update_one({"_id": ObjectId(member_id)}, update_doc)
            return True
        except:
            return False

    def delete_member(self, member_id):
        try:
            self.members_coll.delete_one({"_id": ObjectId(member_id)})
            return True
        except:
            return False

    def mark_attendance(self, member_id, date=None):
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
        try:
            self.members_coll.update_one(
                {"_id": ObjectId(member_id)},
                {"$addToSet": {"attendance": date}}
            )
            return True
        except:
            return False

    def get_attendance(self):
        # Flatten attendance
        members = self.members_coll.find({"attendance": {"$not": {"$size": 0}}})
        logs = []
        for m in members:
            for date in m.get('attendance', []):
                logs.append({
                    "id": str(m['_id']) + "_" + date,
                    "check_in_time": date,
                    "name": m['name'],
                    "member_id": str(m['_id'])
                })
        logs.sort(key=lambda x: x['check_in_time'], reverse=True)
        return logs

    def get_member_attendance(self, member_id):
        member = self.get_member(member_id)
        if not member: return []
        logs = []
        for date in member.get('attendance', []):
            logs.append({"date": date})
        logs.sort(key=lambda x: x['date'], reverse=True)
        return logs

    def get_plans(self, plan_type="workout"):
        plans = list(self.plans_coll.find({"type": plan_type}))
        for p in plans:
            p['_id'] = str(p['_id'])
        return plans

    def add_plan(self, name, details, plan_type="workout"):
        self.plans_coll.insert_one({"name": name, "details": details, "type": plan_type})
        return True

    def delete_plan(self, plan_id):
        self.plans_coll.delete_one({"_id": ObjectId(plan_id)})
        return True

    def delete_attendance(self, attendance_id):
        try:
            member_id, date = attendance_id.split('_')
            self.members_coll.update_one(
                {"_id": ObjectId(member_id)},
                {"$pull": {"attendance": date}}
            )
            return True
        except:
            return False
