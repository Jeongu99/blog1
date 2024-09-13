from . import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

class User(db.Model):
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)