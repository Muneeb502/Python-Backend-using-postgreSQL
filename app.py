from flask import Flask ,request,jsonify

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLAlCHEMY_DATABASE_URL"] = "postgresql://postgres:root@localhost:5433/flask_database"

db = SQLAlchemy(app)

class task(db.Model):
    id = db.Column(db.Integer , primay_key = True ,autoincrement = True )
    name = db.Column( db.String(200) , nullable = False  )
    done = db.Column ( db.Boolean , default = False )


with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return jsonify({"name": "yes your application is working"})


if __name__ == "__main__":
    app.run(debug=True, port=5021)

