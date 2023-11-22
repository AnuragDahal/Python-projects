from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_database.db"
db=SQLAlchemy(app)



class User(db.Model):
    name=db.Column(db.String(200),unique=True,nulllable=False,primary_key=True)
    email=db.Column(db.String(200),unique=True,nulllable=False)
    password=db.Column(db.String(200),nullable=False,primary_key=True)
    id=db.Column(db.Integer,primary_key=True)
    
    def __repr__(self):
        return '<User %r>' % self.name
    
@app.route('/')
def index():
    


app.run(debug=True,port=5002)