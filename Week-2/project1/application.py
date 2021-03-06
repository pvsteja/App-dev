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
	if 'username' not in session :
		return redirect(url_for('register'))
	elif session['username'] :
		return render_template("logout.html")

@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for('register'))
	
@app.route("/register", methods = ["GET", "POST"])
def register():

	if request.method == "GET":
		return render_template("RegistrationWebApp.html")
	elif request.form['action'] == 'register':
		user = request.form.get("username")
		password = request.form.get("pwd")
		# print("username:", user)
		timestamp = datetime.datetime.now()
		user = users(user=user, password=password,time=timestamp)
		try:
			db.session.add(user)
			db.session.commit()
			return render_template("response.html", flag3 = 1)
		except exc.IntegrityError:
			return render_template("RegistrationWebApp.html", flag = flag)
	elif request.form['action'] == 'Login':
		return authentication()
	
@app.route("/auth", methods = ["GET", "POST"])
def authentication():
	if request.method == "POST":
		name = request.form.get("username")
		password = request.form.get("pwd")
		userobject = users.query.get(name)
		if userobject:
			if password == userobject.password:
				# print(name, password)
				session["username"] = name
				return redirect(url_for('index'))
			else :
				return render_template("RegistrationWebApp.html", flag1 = 1)
		else :
			return render_template("RegistrationWebApp.html", flag2 = 1)
@app.route("/admin")
def admin():
	user = users.query.order_by(users.time).all()
	# user_data = db.query(User)
	return render_template("usersdatabase.html", user=user)
