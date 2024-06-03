from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:root@localhost:5433/flask_database"

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    course = db.Column(db.String(200), nullable=False)
    fee = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"name": "yes your application is working"})

@app.route("/tasks")
def showtask():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "title": task.title, "course": task.course, "fee": task.fee} for task in tasks]
    return jsonify({"tasks are shown": task_list})

if __name__ == "__main__":
    app.run(debug=True, port=5021)