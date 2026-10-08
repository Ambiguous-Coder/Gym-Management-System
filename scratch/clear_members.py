from db_manager import DBManager

def clear_all_members():
    db = DBManager()
    result = db.members_coll.delete_many({})
    print(f"Deleted {result.deleted_count} members.")

if __name__ == "__main__":
    clear_all_members()
