import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("C:\\Users\\Ajay\\Desktop\\Try\\serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-1d4c1-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Aryan Chanana",
            "major": "CSE",
            "starting_year": 2021,
            "total_attendance": 6,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-06-14 09:10:23"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-06-14 09:10:23"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2022,
            "total_attendance": 3,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-06-14 09:10:23"
        },
}

for key, value in data.items():
    ref.child(key).set(value)