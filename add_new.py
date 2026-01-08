import streamlit as st
import cv2
import numpy as np
import pickle
import os
import face_recognition
from datetime import datetime

# ---------------- SETUP ----------------
st.set_page_config(
    page_title="Face Registration System",
    layout="centered"
)

os.makedirs("data", exist_ok=True)

faces_file = "data/faces_data.pkl"
names_file = "data/names.pkl"
info_file = "data/user_info.pkl"

# Load Haar Cascade
facedetect = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- UI ----------------
st.title("🧑‍💻 Face Registration Dashboard")
st.markdown("Register a new user by capturing face data")

with st.form("user_form"):
    name = st.text_input("👤 Name")
    enrollment_no = st.text_input("🎓 Enrollment Number")
    roll_no = st.text_input("📄 Roll Number")
    class_name = st.text_input("🏫 Class")
    submit = st.form_submit_button("Start Face Capture")

# ---------------- SESSION STATE ----------------
if "capturing" not in st.session_state:
    st.session_state.capturing = False
if "encodings" not in st.session_state:
    st.session_state.encodings = []

# ---------------- START CAPTURE ----------------
if submit:
    if not all([name, enrollment_no, roll_no, class_name]):
        st.error("❌ Please fill all fields")
    else:
        st.session_state.capturing = True
        st.session_state.encodings = []
        st.success("📸 Camera started. Look at the camera")

# ---------------- CAMERA LOOP ----------------
frame_placeholder = st.empty()
counter_placeholder = st.empty()
stop_button = st.empty()

if st.session_state.capturing:
    video = cv2.VideoCapture(0)

    stop = stop_button.button("⛔ Stop Capture")

    while st.session_state.capturing:
        ret, frame = video.read()
        if not ret:
            st.error("Camera not accessible")
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            enc = face_recognition.face_encodings(
                rgb, [(y, x+w, y+h, x)]
            )
            if enc:
                st.session_state.encodings.append(enc[0])

            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        frame_placeholder.image(frame, channels="BGR")
        counter_placeholder.info(
            f"Captured Faces: {len(st.session_state.encodings)} / 100"
        )

        if stop or len(st.session_state.encodings) >= 100:
            st.session_state.capturing = False
            break

    video.release()

# ---------------- SAVE DATA ----------------
if not st.session_state.capturing and len(st.session_state.encodings) > 0:

    encodings_np = np.array(st.session_state.encodings)

    # Save names
    if os.path.exists(names_file):
        with open(names_file, "rb") as f:
            names = pickle.load(f)
    else:
        names = []

    names.extend([name] * len(encodings_np))

    with open(names_file, "wb") as f:
        pickle.dump(names, f)

    # Save faces
    if os.path.exists(faces_file):
        with open(faces_file, "rb") as f:
            faces = pickle.load(f)
        faces = np.append(faces, encodings_np, axis=0)
    else:
        faces = encodings_np

    with open(faces_file, "wb") as f:
        pickle.dump(faces, f)

    # Save user info
    if os.path.exists(info_file):
        with open(info_file, "rb") as f:
            user_info = pickle.load(f)
    else:
        user_info = []

    user_info.append({
        "name": name,
        "Enroll": enrollment_no,
        "Roll": roll_no,
        "Class": class_name,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    with open(info_file, "wb") as f:
        pickle.dump(user_info, f)

    st.success(f"✅ Successfully registered {name}")
    st.balloons()

    st.session_state.encodings = []
