from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['GymManagementDB']
users_coll = db['users']

result = users_coll.update_one({"username": "admin"}, {"$set": {"password": "123456"}})
if result.modified_count > 0:
    print("Admin password updated to 123456")
else:
    print("Admin password already 123456 or user not found")
