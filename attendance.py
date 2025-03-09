import cv2
import pickle
import numpy as np
import face_recognition
import os
import datetime
import pyttsx3  # Text-to-Speech module

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speech speed

# Load stored face data and labels
faces_file = 'data/faces_data.pkl'
names_file = 'data/names.pkl'
info_file = 'data/user_info.pkl'
attendance_file = 'Attendance/attendance.csv'

if os.path.exists(faces_file) and os.path.exists(names_file) and os.path.exists(info_file):
    with open(faces_file, 'rb') as f:
        known_face_encodings = pickle.load(f)

    with open(names_file, 'rb') as f:
        known_face_names = pickle.load(f)

    with open(info_file, 'rb') as f:
        user_info = pickle.load(f)  # List of dictionaries
else:
    print("❌ Error: No face data found! Run the face registration script first.")
    exit()

# Ensure attendance file exists
if not os.path.exists(attendance_file):
    with open(attendance_file, 'w') as f:
        f.write("Name, Enrollment No, Roll No, Class, Time\n")

# Create a mapping of name → user details
user_details = {info["name"]: info for info in user_info}

# Open webcam
video = cv2.VideoCapture(0)
facedetect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

attendance_marked = set()  # Store marked attendance to avoid duplicates

while True:
    ret, frame = video.read()
    if not ret:
        print("❌ Error: Could not capture frame.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    recognized_name = "Unknown"

    for (x, y, w, h) in faces:
        face_img = frame[y:y + h, x:x + w]
        face_encoding = face_recognition.face_encodings(rgb_frame, [(y, x + w, y + h, x)])

        if face_encoding:
            face_encoding = face_encoding[0]
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

            best_match_index = np.argmin(face_distances) if any(matches) else None

            if best_match_index is not None and matches[best_match_index]:
                recognized_name = known_face_names[best_match_index]

        # Display recognized name
        cv2.putText(frame, recognized_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display message on screen
    cv2.putText(frame, "Press 'o' to mark attendance", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Face Recognition", frame)

    key = cv2.waitKey(1) & 0xFF

    # Mark attendance on pressing 'o'
    if key == ord('o') and recognized_name != "Unknown" and recognized_name not in attendance_marked:
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if recognized_name in user_details:
            details = user_details[recognized_name]
            enrollment_no = details["Enroll"]
            roll_no = details["Roll"]
            class_name = details["Class"]
        else:
            enrollment_no = "Unknown"
            roll_no = "Unknown"
            class_name = "Unknown"

        with open(attendance_file, 'a') as f:
            f.write(f"{recognized_name}, {enrollment_no}, {roll_no}, {class_name}, {current_time}\n")

        # ✅ Print & Speak Name + Attendance Marked
        message = f"{recognized_name} - Attendance Marked ✅"
        print(message)
        engine.say(message)  # Text-to-Speech announcement
        engine.runAndWait()

        # ✅ Show "Attendance Marked" on the Camera Window
        cv2.putText(frame, message, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
        cv2.imshow("Face Recognition", frame)
        cv2.waitKey(1000)  # Wait for 1 second to show the message

        attendance_marked.add(recognized_name)  # Prevent duplicate marking

    # Exit program on pressing 'q'
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
