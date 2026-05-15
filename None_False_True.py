age = int(input("Age: "))
has_license = None
has_insurance = None

while has_license == None:
    license_input = input("Do user have driving licence? (y / n) ")
    if license_input == "y":
        has_license = True
    elif license_input == "n":
        has_license = False

while has_insurance == None:
    insurance_input = input("Do user have insurance? (y / n) ")
    if insurance_input == "y":
        has_insurance = True
    elif insurance_input == "n":
        has_insurance = False

result = age >= 18 and has_license and has_insurance # Complete this line to check if all conditions are met

print(result)