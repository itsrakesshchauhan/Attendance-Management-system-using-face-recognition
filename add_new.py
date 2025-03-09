import cv2
import pickle
import numpy as np
import os
import face_recognition  # Added for better face encoding

# Ensure the 'data' directory exists
os.makedirs('data', exist_ok=True)

# Initialize video capture
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

encodings_list = []
i = 0

# Collect user details
name = input("Enter Your Name: ")
enrollment_no = input("Enter Enrollment No: ")
roll_no = input("Enter Roll No: ")
class_name = input("Enter Class: ")

while True:
    ret, frame = video.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB (face_recognition requires RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y + h, x:x + w]
        face_encoding = face_recognition.face_encodings(rgb_frame, [(y, x + w, y + h, x)])

        if face_encoding:
            encodings_list.append(face_encoding[0])  # Store the face encoding

        i += 1
        cv2.putText(frame, f"Captured: {len(encodings_list)}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

    cv2.imshow("Frame", frame)

    # Stop when 100 encodings are collected or 'q' is pressed
    if cv2.waitKey(1) == ord('q') or len(encodings_list) >= 100:
        break

video.release()
cv2.destroyAllWindows()

# Convert encodings to NumPy array
encodings_list = np.array(encodings_list)

# File paths
faces_file = 'data/faces_data.pkl'
names_file = 'data/names.pkl'
info_file = 'data/user_info.pkl'

# Save faces and names ensuring consistency
if os.path.exists(names_file):
    with open(names_file, 'rb') as f:
        names = pickle.load(f)
    names += [name] * len(encodings_list)  # Ensure same length as encodings
else:
    names = [name] * len(encodings_list)

with open(names_file, 'wb') as f:
    pickle.dump(names, f)

if os.path.exists(faces_file):
    with open(faces_file, 'rb') as f:
        faces = pickle.load(f)
    faces = np.append(faces, encodings_list, axis=0)
else:
    faces = encodings_list

with open(faces_file, 'wb') as f:
    pickle.dump(faces, f)

# Save additional user info
if os.path.exists(info_file):
    with open(info_file, 'rb') as f:
        user_info = pickle.load(f)
else:
    user_info = []

user_info.append({'name': name, 'Enroll': enrollment_no, 'Roll': roll_no, 'Class': class_name})

with open(info_file, 'wb') as f:
    pickle.dump(user_info, f)

print(f"✅ Successfully saved {len(encodings_list)} face encodings and user details!")
