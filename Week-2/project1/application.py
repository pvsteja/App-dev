import os
import datetime
# import bcrypt
from models import *

from flask import Flask, session, render_template, request, redirect, url_for
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# # Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
	return "Project 1: TODO"

@app.route("/register", methods = ["GET", "POST"])
def register():

	if request.method == "GET":
		return render_template("RegistrationWebApp.html")
	elif request.form['action'] == 'register':
		user = request.form.get("username")
		password = request.form.get("pwd")
		print("name:", user)
		timestamp = datetime.datetime.now()
		user = users(user=user, password=password,time=timestamp)
		try:
			db.session.add(user)
			db.session.commit()
			return render_template("response.html", user = user)
		except exc.IntegrityError:
			return render_template("RegistrationWebApp.html")

@app.route("/admin")
def table():
	user = users.query.order_by(users.time).all()
	# user_data = db.query(User)
	return render_template("usersdatabase.html", user=user)