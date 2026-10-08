-- database_schema.sql
CREATE DATABASE IF NOT EXISTS gym_os;
USE gym_os;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'admin'
);

-- Insert default admin
INSERT IGNORE INTO users (username, password, role) VALUES ('admin', '123456', 'admin');

CREATE TABLE IF NOT EXISTS members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(100),
    join_date DATE,
    weight DECIMAL(5,2),
    height DECIMAL(5,2),
    bmi DECIMAL(5,2),
    body_fat DECIMAL(5,2),
    workout_plan VARCHAR(255),
    trainer_remarks TEXT,
    custom_schedule TEXT,
    fitness_goal VARCHAR(50),
    daily_calories INT,
    macro_split VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS attendance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT,
    check_in_time DATETIME,
    FOREIGN KEY (member_id) REFERENCES members(id) ON DELETE CASCADE
);
