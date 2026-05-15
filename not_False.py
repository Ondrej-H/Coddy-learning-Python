# Checking if a person is NOT (a student or employed)
is_student = False
is_employed = False

# These two expressions are equivalent:
result1 = not (is_student or is_employed)
result2 = (not is_student) and (not is_employed)

print(result1)  # True
print(result2)  # True