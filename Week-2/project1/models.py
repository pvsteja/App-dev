from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
class users(db.Model):
	__tablename__ = "usercredentials"
	user = db.Column(db.String, primary_key=True)
	password = db.Column(db.String, nullable=False)
	time = db.Column(db.DateTime(), nullable=False)

	def __init__(self, user, password, time):
		self.user = user
		self.password = password
		self.time = time

class Book(db.Model):
	__tablename__ = "books"
	ISBN = db.Column(db.String, primary_key=True)
	title = db.Column(db.String, nullable=False)
	author = db.Column(db.String, nullable=False)
	year = db.Column(db.String, nullable=False)

	def __init__(self, ISBN, title, author, year):
		self.ISBN = ISBN
		self.title = title
		self.author = author
		self.year = year

