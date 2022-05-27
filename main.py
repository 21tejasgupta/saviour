from flask import Flask,render_template
import cv2
from simplefacerec import SimpleFacerec
import subprocess as sp

app=Flask(__name__)
# Encode faces from a folder
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

@app.route('/')
@app.route('/home')
def home():
    return render_template('main_index.html')

@app.route('/index.php')
def phpindex():
    out=sp.run(["php","index.php"],stdout=sp.PIPE)
    return out.stdout

if __name__=="__main__":
    app.run(debug=True)

