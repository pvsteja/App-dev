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