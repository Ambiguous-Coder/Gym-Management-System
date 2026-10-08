import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'gym_os'
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE members ADD COLUMN IF NOT EXISTS custom_schedule TEXT;")
    cursor.execute("ALTER TABLE members ADD COLUMN IF NOT EXISTS fitness_goal VARCHAR(50);")
    cursor.execute("ALTER TABLE members ADD COLUMN IF NOT EXISTS daily_calories INT;")
    cursor.execute("ALTER TABLE members ADD COLUMN IF NOT EXISTS macro_split VARCHAR(50);")
    conn.commit()
    conn.close()
    print("Database patched successfully with custom_schedule column.")
except Exception as e:
    print(f"Failed to patch db (Column might already exist): {e}")
