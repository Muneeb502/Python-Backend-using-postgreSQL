from flask import Flask ,request,jsonify

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLAlCHEMY_DATABASE_URL"] = "postgresql://postgres:root@localhost:5433/flask_database"


@app.route("/")
def home():
    return jsonify({"name": "yes your application is working"})


if __name__ == "__main__":
    app.run(debug=True, port=5021)

