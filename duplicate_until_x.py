"""
Create a function named duplicate_until_x that receives string as its parameter.

This function aims to duplicate each character in the given string up until the first occurrence of the character 'x'. If 'x' is not present in the string, the function should return the original string unchanged.

To solve this challenge, you can iterate through each character in the string. For each character, check if it is not 'x'. If it's not 'x', duplicate the character and append it to a new string. If the character is 'x', append it to the new string and then append the remaining characters from the original string (including 'x') to the new string without duplication. Finally, return the new string.

Parameters:

string (str): The input string that needs to be processed.
The function returns a string where each character is duplicated up until the first occurrence of 'x'. If 'x' is not present, the original string is returned unchanged.
"""


def duplicate_until_x(string):
    # Write code here
    new_string = ""
    if "x" not in string:
        new_string = string
    
    else:
        for indx in range(len(string)):
            
            if string[indx] == "x":
                new_string += "x"
                new_string += string[indx:]
                break

            else:
                new_string += string[indx] * 2

    return new_string
        

"""# test
string = "Ahoxoj"
print(duplicate_until_x(string))"""
            