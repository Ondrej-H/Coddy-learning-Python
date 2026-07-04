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

def add_student(student_records: dict, name: str, age: int, courses: list[str]) -> None:
    if name in student_records:
        print(f"Student '{name}' already exists.")
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
    
    return course in student_records[name]["courses"]
    

def calculate_average_grade(name: str) -> float | None:
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    
    grades = student_records[name]["grades"]

    if not grades:
        return 0
    
    average_grade = sum(grades) / len(grades)

    return average_grade


def list_students_by_course(course: str) -> list[str]:
    list_of_students_in_course = []
    
    for student in student_records:

        if course in student_records[student]["courses"]:                
            list_of_students_in_course.append(student)
        
    return list_of_students_in_course


def filter_top_students(threshold: float) -> list[str]:
    list_of_top_students = []

    for student in student_records:
        if calculate_average_grade(student) > threshold:
            list_of_top_students.append(student)

    return list_of_top_students

            

add_student(student_records, "Alice", 20, ["Math", "Physics"])
add_student(student_records, "Bob", 22, ["Math", "Biology"])
add_student(student_records, "Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Should return ["Alice", "Diana"]
print(filter_top_students(90))  # Should return ["Diana"]
print(filter_top_students(100))  # Should return an empty list
