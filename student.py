from database import get_connection

def add_student(roll, name, age, course):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (roll, name, age, course)
        )
        conn.commit()
        print(" Student added successfully")
    except:
        print(" Roll number already exists")
    finally:
        conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if students:
        print("\nRoll | Name | Age | Course")
        print("-" * 30)
        for s in students:
            print(s)
    else:
        print("No students found")

    conn.close()

def search_student(roll):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE roll = ?", (roll,))
    student = cursor.fetchone()

    if student:
        print(" Student Found:", student)
    else:
        print(" Student not found")

    conn.close()

def update_student(roll, name, age, course):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE roll=?",
        (name, age, course, roll)
    )

    if cursor.rowcount:
        print(" Student updated successfully")
    else:
        print("Student not found")

    conn.commit()
    conn.close()

def delete_student(roll):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE roll=?", (roll,))

    if cursor.rowcount:
        print("Student deleted successfully")
    else:
        print(" Student not found")

    conn.commit()
    conn.close()
