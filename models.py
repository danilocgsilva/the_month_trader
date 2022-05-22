'''
User
'''

from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    name = db.Column(db.String(256))

class Symbol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(16))
