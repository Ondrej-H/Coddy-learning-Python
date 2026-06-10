# Step 1: Create the Grades Dictionary
grades = {
    # Add initial student grades here
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}

# Step 2: Access All Keys and Values
# Print all students and grades
print("Students:", grades.keys())
print("Grades:", grades.values())

# Step 3: Add a New Student
# Add Diana with a grade of 92
grades["Diana"] = 92

# Step 4: Retrieve a Student's Grade
# Get Bob's grade using get() 
#bobs_grade = grades["Bob"]
bobs_grade = grades.get("Bob")
print("Bob's grade:", bobs_grade)

# Step 5: Remove a Student
# Remove Charlie using pop() method
grades.pop("Charlie")
# Print the updated dictionary
print("Updated grades:", grades)