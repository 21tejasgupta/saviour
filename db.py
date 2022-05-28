from flask import Flask,render_template,request,redirect,url_for
import cv2
import subprocess as sp
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tb_users.db'
#initil=alize database
DB=SQLAlchemy(app)

#create db model
class User(DB.Model):
    id=DB.Column(DB.Integer, primary_key=True)
    fname=DB.Column(DB.String(200),nullable=False)
    lname=DB.Column(DB.String(200),nullable=False)
    address=DB.Column(DB.String(200),nullable=False)
    phone=DB.Column(DB.Integer,nullable=False)
    email=DB.Column(DB.String(200),nullable=False)
    fname2=DB.Column(DB.String(200),nullable=False)
    lname2=DB.Column(DB.String(200),nullable=False)
    address2=DB.Column(DB.String(200),nullable=False)
    phone2=DB.Column(DB.Integer,nullable=False)
    email2=DB.Column(DB.String(200),nullable=False)
    #date_created=db.Column(db.DateTime,default=datetime.utcnow)
    #create function to return string when we add something
    def _repr_(self):
        return f"User('{self.id}','{self.fname},'{self.lname}','{self.address}','{self.phone}','{self.email}',,'{self.fname2},'{self.lname2}','{self.address2}','{self.phone2}','{self.email2}')"

   
