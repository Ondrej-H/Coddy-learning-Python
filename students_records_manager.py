'''
Create a function named add_student that takes three arguments:
name (string), age (integer), and courses (a list of strings).

The function should:
Check if the student name already exists in the student_records dictionary.
If it does, print "Student '<name>' already exists.".
If the name does not exist, add it to student_records with age,
an empty set for grades, and a set of courses.
Print "Student '<name>' added successfully.".

Add the following block of code at the bottom of your code:
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
print(student_records)
'''

student_records = {}

def add_student(name: str, age: int, courses: list[str]) -> None:
    if name in student_records:
        print(f"Student {name} already exists.")
        return
    
    student_records[name] = {
        "age": age,
        "grades": set(),
        "courses": set(courses)
    }

    print(f"Student '{name}' added successfully.")


def add_grade(name: str, grade: int) -> None:
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return
    
    student_records[name]["grades"].add(grade)

    print(f"Grade {grade} added for student '{name}'.")


def is_enrolled(name: str, course: str) -> bool:
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return False
    
    if course in student_records[name]["courses"]:
        return True
    
    if course not in student_records[name]["courses"]:
        return False
    

def calculate_average_grade(name: str):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    
    grades = student_records[name]["grades"]

    if not grades:
        return 0
    
    if grades:
        total = 0
        for num in grades:
            total += num
            average_grade = total / len(grades)

        return average_grade


def list_students_by_course

    
add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Biology", "Chemistry"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
print(calculate_average_grade("Alice"))  # Should return 87.5
print(calculate_average_grade("Bob"))  # Should return 75.0
print(calculate_average_grade("Charlie"))  # Non-existent student, should print message and return None
print(calculate_average_grade("Alice"))  # Should return 87.5 again
