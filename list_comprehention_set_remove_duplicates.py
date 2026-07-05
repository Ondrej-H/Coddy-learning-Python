def elements_of_freedom(elements: list[str]) -> list[str]:
    # Your solution here
    
    # Step 1: Filter elements with length >= 5
    # Step 2: Convert filtered elements to uppercase
    filtered_elements = [
        word.upper()
        for word in elements
        if len(word) >= 5]

    # Step 3: Create a list of unique elements
    seen = set()
    unique_elements = []
    for word in filtered_elements:
        if word not in seen:
            seen.add(word)
            unique_elements.append(word)
    
    # Step 4: Return the final result
    return unique_elements


"""input = ["apple", "banana", "cherry", "date", "apple", "banana", "grape", "fig"]
'''Output: ['APPLE', 'BANANA', 'CHERRY', 'GRAPE']'''

print(elements_of_freedom(input))"""