# Attendance-Management-system-using-face-recognition
Face Recognition-Based Attendance System 🎯🎥 90% faster with no raw images data,
This is a real-time face recognition-based attendance system using OpenCV, face_recognition, and Python. It captures faces, stores user details, and marks attendance automatically upon recognition. The system also announces the marked attendance using text-to-speech (TTS) and displays it on the camera screen.

🚀 Features
✅ Face Registration: Capture and store face encodings with name, enrollment number, roll number, and class.
✅ Real-Time Face Recognition: Detects and identifies faces from a live camera feed.
✅ Attendance Marking: Press 'o' to mark attendance when a face is recognized.
✅ Prevents Duplicate Entries: Ensures each person’s attendance is marked only once per session.
✅ Text-to-Speech (TTS) Notification: Announces "Name - Attendance Marked ✅" when attendance is recorded.
✅ On-Screen Display: Shows the recognized name and a message confirming attendance on the webcam feed.
✅ Data Storage: Stores faces in faces_data.pkl, names in names.pkl, and user info in user_info.pkl.
✅ Exports Attendance Record: Attendance is logged in attendance.csv with a timestamp.

🛠 Installation & Setup
1️⃣ Clone the Repository

2️⃣ Install Dependencies

3️⃣ Run Face Registration (To add a new face)
python add_new.py

📌 Follow the instructions to capture your face and input details.

4️⃣ Run Attendance System

python attendance.py

🎥 Press 'o' to mark attendance
🛑 Press 'q' to quit

📂 File Structure
bash
Copy
Edit
📁 face-recognition-attendance/
│── 📂 data/                   # Stores face encodings, names, and user info
│── 📜 add_new.py        # Script to register a new face
│── 📜 attendance.py           # Real-time face recognition and attendance marking
│── 📜 attendance_record.py     # Checks attendance record
│── 📜 README.md               # Project documentation


📌 Usage Instructions

1️⃣ Register Faces 🏷

Run add_new.py
Enter Name, Enrollment No, Roll No, Class
Capture 100 face images  #take less than 1 min

_# It will create three files in data forlder :-- " 1.faces_data.pkl , 2. names.pkl , 3. user_info.pkl "_

2️⃣ Start Attendance System 📸
Run attendance.py
Look at the camera → Face will be recognized
Press 'o' → Attendance will be marked ✅
Press 'q' → Quit the system

3️⃣ Check Attendance Logs 📄
Run attendance_record.py or
Open attendance.csv to see recorded entries.

⚡ Technologies Used
Python 🐍
OpenCV 🎥 (Real-time Face Detection)
Face Recognition 🏷 (Encoding & Matching Faces)
NumPy 🔢 (Array Processing)
Pyttsx3 🎙 (Text-to-Speech Announcement)
Pickle 🗂 (Data Storage)

💡 Future Improvements
🔹 Store attendance in a database (SQL, Firebase, MongoDB)
🔹 Add GUI for better usability
🔹 Implement multi-person recognition

❤️ #**Follow me if you like my work**
