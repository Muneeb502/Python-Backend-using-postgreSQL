from flask import Flask ,request,jsonify

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLAlCHEMY_DATABASE_URL"] = "postgresql://postgres:root@localhost:5433/flask_database"


db = app(SQLAlchemy)


class task(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement = True)
    tittle = db.Column(db.string(200), nullable = False)
    course = db.Column(db.string(200), nullable = False)
    fee = db.Column(db.Boolean, default = False)
with app.app_context():
    db.creat_all()
   

@app.route("/")
def home():
    return jsonify({"name": "yes your application is working"})


@app.route("/tasks")
def showtask():
    tasks = task.query.all()
    task_list = [ {"id":task.id, "tittle": task.tittle, "course": task.course,"fee": task.fee} for task in tasks]
    return jsonify({"tasks are shoe": task_list})


if __name__ == "__main__":
    app.run(debug=True, port=5021)

