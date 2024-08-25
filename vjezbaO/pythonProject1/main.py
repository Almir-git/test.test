

# Array (listu) studenata:
# Svaki student: name "Almir". score: 0-100, active: true/false

students = [
    {
        "name": "Almir",
        "score": 99,
        "active": True
    },
    {
        "name": "Adis",
        "score": 95,
        "active": True
    },
    {
        "name": "Amir",
        "score": 44,
        "active": False
    }
]

# Napisati petlju samo onih ucenika koji su aktivni

for student in students:

    if not student['active']:
        continue

    if student['score'] >= 80:
        student['grade'] = "A"
    elif student['score'] >= 60 and student['score'] <= 80:
        student['grade'] = "B"
    elif student['score'] >= 40 and student['score'] <= 60:
        student['grade'] = "C"
    elif student['score'] >= 20 and student['score'] <= 40:
        student['grade'] = "D"
    else:
        student['grade'] = "E"
print(students)
