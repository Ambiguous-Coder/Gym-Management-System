import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': ''
}

try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    with open('database_schema.sql', 'r') as f:
        sql = f.read()
    
    statements = [s.strip() for s in sql.split(';') if s.strip()]
    for statement in statements:
        try:
            cursor.execute(statement)
        except Exception as e:
            print(f"Statement failed: {e}")
            
    conn.commit()
    conn.close()
    print("Database Initialized Successfully.")
except Exception as e:
    print(f"Failed to connect or initialize: {e}")
