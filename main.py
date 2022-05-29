from tkinter import Entry
from flask import Flask,render_template,request,redirect,url_for
import cv2
from simplefacerec import SimpleFacerec
import subprocess as sp
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import base64
import os
import re
from PIL import Image
from io import StringIO, BytesIO



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tb_users.db'
#initilalize database
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

    def _repr_(self):
        return f"User('{self.id}','{self.fname},'{self.lname}','{self.address}','{self.phone}','{self.email}',,'{self.fname2},'{self.lname2}','{self.address2}','{self.phone2}','{self.email2}')"

   
details=User.query.all()

@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('main_index.html')

@app.route('/storeImage',methods=['POST','GET'])
def storeImage():
    #get last database Entry
    last_entry=User.query.order_by(User.id.desc()).first()
    last_fname=last_entry.fname
    last_lname=last_entry.lname
    last_name=last_fname+" "+last_lname

    image_b64 = request.values['imageBase64']
    image_data = re.sub('^data:image/.+;base64,', '', image_b64)
    image_data = base64.b64decode(str(image_data))
    image_PIL = Image.open(BytesIO(image_data))
    image_save = image_PIL.save('imagespy/'+last_name+'.png')
    return render_template('main_index.html')

@app.route('/scan')
def scan():
    sfr = SimpleFacerec()
    sfr.load_encoding_images("imagespy/")

    # Load Camera
    cap = cv2.VideoCapture(0)


    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    detail=User.query.filter_by(fname=face_names[0].split()[0]).first()
    print(detail)

    return render_template('result.html',detail=detail)


@app.route('/capture',methods=['POST','GET'])
def capture():
    return render_template('capture.html')

@app.route('/register',methods=['POST','GET'])
def register():
    if request.method=='POST':
        print('inside loop')
        registered_fname=request.form['first_name']
        registered_lname=request.form['last_name']
        registered_phone=request.form['phone_number']
        registered_address=request.form['address']
        registered_email=request.form['email']
        registered_fname2=request.form['first_name2']
        registered_lname2=request.form['last_name2']
        registered_phone2=request.form['phone_number2']
        registered_address2=request.form['address2']
        registered_email2=request.form['email2']

        new_details=User(fname=registered_fname,lname=registered_lname,address=registered_address,phone=registered_phone,email=registered_email,fname2=registered_fname2,lname2=registered_lname2,address2=registered_address2,phone2=registered_phone2,email2=registered_email2)

        #push to db table
        #try:
        DB.session.add(new_details)
        DB.session.commit()
        return redirect(url_for('capture'))
            
        #except:
            #return "there was an error adding your details"
        
    else:
        registers =User.query.order_by(User.id)
    return render_template('registration.html')

@app.route('/result')
def result():
   return render_template('result.html',details=details)

    
if __name__=="__main__":
    DB.create_all()
    app.run(debug=True)