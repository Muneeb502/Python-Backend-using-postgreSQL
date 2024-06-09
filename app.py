from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#  configuration key
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5432/flask_database"

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(200), nullable=False)
    fee = db.Column(db.Boolean, default=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"message": "Yes, your application is working"})

@app.route("/tasks")
def show_task():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "course": task.course, "fee": task.fee} for task in tasks]
    return jsonify({"tasks": task_list})

@app.route("/m")
def add_tasks():
    SAMP_TASK = [
        {"title": "Learn Flask", "course": "Web Development", "fee": False},
        {"title": "Learn SQLAlchemy", "course": "Database Management", "fee": True},
        {"title": "Learn PostgreSQL", "course": "Database Management", "fee": False}
    ]
    
    for task_data in sample_tasks:
        task = Task(title=task_data["title"], course=task_data["course"], fee=task_data["fee"])
        db.session.add(task)
    
    db.session.commit()
    return jsonify({"message": "Sample tasks added"}), 201


if __name__ == "__main__":
    app.run(debug=True, port=50501)
