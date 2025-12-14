<div align="center">

# 🎯 Attendance Management System  
## Using Face Recognition 🧠🎥  

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Real--Time-green)
![AI](https://img.shields.io/badge/AI-Face%20Recognition-orange)
![Status](https://img.shields.io/badge/Project-Active-success)

⚡ **90% Faster Attendance | No Raw Images Stored | Real-Time Recognition**

</div>

---

## 📌 Project Overview

A **real-time face recognition–based attendance system** built using **Python**, **OpenCV**, and **face_recognition**.  
The system captures faces, stores **only encodings (no raw images)**, and automatically marks attendance with **audio and visual confirmation**.

---

## 🚀 Features

| Feature | Description |
|------|------------|
| 🧠 Face Registration | Stores face encodings with name, enrollment, roll & class |
| 🎥 Live Recognition | Detects and recognizes faces via webcam |
| ⏱ One-Key Attendance | Press **`o`** to mark attendance |
| 🔐 Duplicate Prevention | Attendance marked once per session |
| 🎙 Text-to-Speech | Announces “Name – Attendance Marked ✅” |
| 📊 CSV Export | Attendance saved with timestamp |

---

## 🛠 Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/Attendance-Management-system-using-face-recognition.git
cd Attendance-Management-system-using-face-recognition 
```

2️⃣ Install Dependencies
```
pip install opencv-python face-recognition numpy pyttsx3
```

### Usage Instructions

Step 1: Register Face
```
python add_new.py
```
📝 Enter:
```
Name

Enrollment Number

Roll Number

Class
```
Captures ~100 face images (< 1 minute)

and Creates files in "data/" Folder
```
faces_data.pkl
names.pkl
user_info.pkl
```
Step 2: Start Attendance System
```
python attendance.py
```
Controls:

o → Mark Attendance ✅

q → Quit System

---

Step 3: Check Attendance Logs
```
python attendance_record.py
```
or

```
open attendance.csv
```
---
## Project Structure
```bash
📁 face-recognition-attendance
│
├── 📂 data
│   ├── faces_data.pkl
│   ├── names.pkl
│   └── user_info.pkl
│
├── add_new.py
├── attendance.py
├── attendance_record.py
├── attendance.csv
└── README.md
```
---
## Technologies Used
| Technology          | Purpose                  |
| ------------------- | ------------------------ |
| 🐍 Python           | Core Logic               |
| 🎥 OpenCV           | Face Detection           |
| 🧠 face_recognition | Face Encoding & Matching |
| 🔢 NumPy            | Numerical Processing     |
| 🎙 pyttsx3          | Text-to-Speech           |
| 🗂 Pickle           | Data Storage             |

---
### Future Improvement
1. 🗄 Database Integration (MySQL / MongoDB / Firebase)

2. 🖥 GUI Interface

3. 👥 Multi-Person Recognition

4. ☁ Cloud Attendance Sync
---
<div align="center">
❤️ Like this project?
⭐ Star the repo & Follow me on GitHub
</div> ```


