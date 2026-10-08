from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from bson import ObjectId
from db_manager import DBManager
from data_manager import WORKOUT_CLASSES
from datetime import datetime
import random
from diet_manager import generate_diet_plan

app = Flask(__name__)
app.secret_key = 'gym_os_secret_123'
db = DBManager()

MOTIVATIONAL_QUOTES = [
    "Success starts with self-discipline.",
    "Your only limit is you.",
    "Don't stop when you're tired. Stop when you're done.",
    "Focus on your goal. Don't look in any direction but forward.",
    "The body achieves what the mind believes.",
    "Hard work beats talent when talent doesn't work hard.",
    "Push yourself, because no one else is going to do it for you.",
    "Sometimes later becomes never. Do it now."
]

@app.route('/')
def index():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if db.verify_login(username, password):
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session: return redirect(url_for('login'))
    stats = db.get_dashboard_stats()
    members = db.get_members()
    current_day = datetime.now().strftime("%A")
    quote = random.choice(MOTIVATIONAL_QUOTES)
    return render_template('dashboard.html', stats=stats, current_day=current_day, 
                           workout_classes=WORKOUT_CLASSES, members=members, quote=quote)

@app.route('/workouts', methods=['GET', 'POST'])
def workouts():
    if 'user' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        schedule = {}
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            focus = request.form.get(f'focus_{day}', '')
            ex_str = request.form.get(f'exercises_{day}', '')
            exercises = [e.strip() for e in ex_str.split(',') if e.strip()]
            schedule[day] = {"focus": focus, "exercises": exercises}
        
        details = {"range": "Custom", "badge": "Custom", "schedule": schedule}
        db.add_plan(name, details, "workout")
        flash('Workout plan added!', 'success')
        return redirect(url_for('workouts'))

    current_day = datetime.now().strftime("%A")
    plans = db.get_plans("workout")
    return render_template('workouts.html', plans=plans, current_day=current_day)

@app.route('/workouts/delete/<string:plan_id>', methods=['POST'])
def delete_workout_plan(plan_id):
    if 'user' not in session: return redirect(url_for('login'))
    db.delete_plan(plan_id)
    flash('Workout plan deleted.', 'success')
    return redirect(url_for('workouts'))

@app.route('/edit_workout/<string:plan_id>', methods=['GET', 'POST'])
def edit_workout_plan(plan_id):
    if 'user' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        schedule = {}
        for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
            focus = request.form.get(f'focus_{day}', '')
            ex_str = request.form.get(f'exercises_{day}', '')
            exercises = [e.strip() for e in ex_str.split(',') if e.strip()]
            schedule[day] = {"focus": focus, "exercises": exercises}
        
        update_doc = {
            "name": name,
            "details.schedule": schedule
        }
        
        if db.plans_coll.update_one({"_id": ObjectId(plan_id)}, {"$set": update_doc}):
            flash('Workout plan updated!', 'success')
        else:
            flash('Failed to update workout plan.', 'error')
        return redirect(url_for('workouts'))

    plan = db.plans_coll.find_one({"_id": ObjectId(plan_id)})
    if not plan:
        flash('Plan not found.', 'error')
        return redirect(url_for('workouts'))
    
    plan['_id'] = str(plan['_id'])
    return render_template('edit_workout.html', plan=plan)

@app.route('/diets', methods=['GET', 'POST'])
def diets():
    if 'user' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        meals = {
            "breakfast": request.form['breakfast'],
            "lunch": request.form['lunch'],
            "dinner": request.form['dinner'],
            "snacks": request.form['snacks']
        }
        db.add_plan(name, meals, "diet")
        flash('Diet plan added!', 'success')
        return redirect(url_for('diets'))

    plans = db.get_plans("diet")
    # Fallback to templates if no custom diets exist yet
    if not plans:
        diet_templates = {
            'Muscle Gain':    {'goal': 'Muscle Gain',    'bmi': 22, 'info': generate_diet_plan(22, 'Muscle Gain')},
            'Weight Loss':    {'goal': 'Weight Loss',    'bmi': 32, 'info': generate_diet_plan(32, 'Weight Loss')},
            'Maintenance':    {'goal': 'Maintenance',    'bmi': 23, 'info': generate_diet_plan(23, 'Maintenance')},
        }
    else:
        diet_templates = {p['name']: {'goal': p['name'], 'info': p['details']} for p in plans}
        
    return render_template('diets.html', diet_templates=diet_templates, plans=plans)

@app.route('/diets/delete/<string:plan_id>', methods=['POST'])
def delete_diet_plan(plan_id):
    if 'user' not in session: return redirect(url_for('login'))
    db.delete_plan(plan_id)
    flash('Diet plan deleted.', 'success')
    return redirect(url_for('diets'))

@app.route('/members', methods=['GET', 'POST'])
def members():
    if 'user' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        if db.add_member(request.form):
            flash('Member created successfully!', 'success')
        else:
            flash('Failed to create member.', 'error')
        return redirect(url_for('members'))
        
    search = request.args.get('q')
    members_list = db.get_members(search)
    return render_template('members.html', members=members_list)

@app.route('/members/<string:member_id>/profile', methods=['GET', 'POST'])
def profile(member_id):
    if 'user' not in session: return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Handle regular profile update
        if 'name' in request.form:
            if db.update_member(member_id, request.form):
                flash('Profile updated successfully!', 'success')
            else:
                flash('Failed to update profile.', 'error')
        # Handle plan override
        elif 'workout_routine' in request.form:
            routine_name = request.form['workout_routine']
            update_data = {
                "workout_routine": routine_name,
                "personal_workout": WORKOUT_CLASSES.get(routine_name, {}).get('schedule', {}),
                "diet_plan.breakfast": request.form['diet_breakfast'],
                "diet_plan.lunch": request.form['diet_lunch'],
                "diet_plan.dinner": request.form['diet_dinner'],
                "diet_plan.snacks": request.form['diet_snacks']
            }
            if db.members_coll.update_one({"_id": ObjectId(member_id)}, {"$set": update_data}):
                flash('Plans updated successfully!', 'success')
            else:
                flash('Failed to update plans.', 'error')
        # Handle custom schedule override
        elif 'customize_workout' in request.form:
            schedule = {}
            for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                focus = request.form.get(f'focus_{day}', '')
                ex_str = request.form.get(f'exercises_{day}', '')
                exercises = [e.strip() for e in ex_str.split(',') if e.strip()]
                schedule[day] = {"focus": focus, "exercises": exercises}
            
            if db.members_coll.update_one({"_id": ObjectId(member_id)}, {"$set": {"personal_workout": schedule}}):
                flash('Custom schedule saved!', 'success')
            else:
                flash('Failed to save custom schedule.', 'error')
                
        return redirect(url_for('profile', member_id=member_id))
        
    member = db.get_member(member_id)
    if not member:
        flash('Member not found.', 'error')
        return redirect(url_for('members'))
    
    # Ensure personal_workout exists to avoid Jinja2 UndefinedError
    if 'personal_workout' not in member:
        member['personal_workout'] = {}
        
    current_day = datetime.now().strftime("%A")
    attendance_history = db.get_member_attendance(member_id)
    return render_template('profile.html', member=member, workout_classes=WORKOUT_CLASSES, 
                           current_day=current_day, attendance_history=attendance_history)



@app.route('/members/<string:member_id>/delete', methods=['POST'])
def delete_member(member_id):
    if 'user' not in session: return redirect(url_for('login'))
    if db.delete_member(member_id):
        flash('Member deleted successfully.', 'success')
    else:
        flash('Failed to delete member.', 'error')
    return redirect(url_for('members'))

@app.route('/attendance', methods=['GET'])
def attendance():
    if 'user' not in session: return redirect(url_for('login'))
    logs = db.get_attendance()
    members_list = db.get_members()
    current_day_date = datetime.now().strftime('%Y-%m-%d')
    return render_template('attendance.html', logs=logs, members=members_list, current_day_date=current_day_date)

@app.route('/attendance/mark', methods=['POST'])
def mark_attendance():
    if 'user' not in session: return redirect(url_for('login'))
    member_id = request.form['member_id']
    date = request.form.get('date') or datetime.now().strftime('%Y-%m-%d')
    if db.mark_attendance(member_id, date):
        flash('Attendance marked successfully!', 'success')
    else:
        flash('Failed to mark attendance.', 'error')
    return redirect(url_for('attendance'))

@app.route('/attendance/<string:attendance_id>/delete', methods=['POST'])
def delete_attendance(attendance_id):
    if 'user' not in session: return redirect(url_for('login'))
    if db.delete_attendance(attendance_id):
        flash('Attendance record deleted.', 'success')
    else:
        flash('Failed to delete attendance.', 'error')
    return redirect(url_for('attendance'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
