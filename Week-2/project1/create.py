import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
os.environ["DATABASE_URL"] = "postgres://wwgchdfoipxweb:6f944eb3a2278561cc5e9ffe3144e89104f144429ec4f7b87cce9ffa0c0e3a66@ec2-54-197-48-79.compute-1.amazonaws.com:5432/d48jjugm82ikeu"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
