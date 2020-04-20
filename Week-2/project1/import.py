import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
	file = open("books.csv")
	books = csv.reader(file)
	# adding all values to book object
	for ISBN, title, author, pubyear in books:
		obj = Book(ISBN=ISBN, title=title, author=author, year=pubyear)
		db.session.add(obj)
	db.session.commit()

if __name__ == '__main__':
	with app.app_context():
	main()

