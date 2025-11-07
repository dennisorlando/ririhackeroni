import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

database_url = os.getenv("DATABASE_URL")
if not database_url:
    user = os.getenv("POSTGRES_USER", "flaskuser")
    pw = os.getenv("POSTGRES_PASSWORD", "flaskpassword")
    host = os.getenv("POSTGRES_HOST", "db")
    port = os.getenv("POSTGRES_PORT", "5432")
    db   = os.getenv("POSTGRES_DB", "flaskdb")
    database_url = f"postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}"

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route("/health")
def health():
    return jsonify(status="ok")

@app.route("/")
def index():
    return jsonify(message="Kittens in a box")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
