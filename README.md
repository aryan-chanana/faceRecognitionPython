# 🎯 Real-Time Face Attendance System using Python & Firebase

A Python-based project that marks attendance in real time using face recognition with Firebase backend integration.

## ✅ What It Does

- Uses webcam to detect and recognize student faces
- Matches face encodings stored locally (`EncodeFile.p`)
- Fetches student data (name, attendance, etc.) from Firebase Realtime DB
- Displays student photo (from Firebase Storage)
- Updates attendance in the database with timestamp logic
- UI overlays are used for feedback and interaction

---

## 🔧 Tech Stack

- Python 3.x
- OpenCV
- face_recognition
- Firebase Admin SDK
- NumPy
- cvzone (for styled overlays)

---

## 🗂️ Project Structure

```
faceRecognitionPython/
├── Images/                    # Contains student face images
├── Resources/
│   ├── Modes/                 # Mode images (for UI)
│   └── background.png         # Background image for main UI
├── EncodeFile.p              # Pickle file storing known face encodings
├── EncodeGenerator.py        # Script to generate encodings and push to Firebase
├── AddDataToDatabase.py      # Script to manually add student data to Firebase Realtime DB
├── main.py                   # Main file for running face recognition and attendance
├── .gitignore                # Git ignore file (excludes secrets)
├── README.md                 # Project documentation
└── CREDITS.md                # Attributions and external resources
```
