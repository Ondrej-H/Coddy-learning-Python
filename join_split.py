data = "x:y:z"

print(data.split(':'))
print(''.join(data.split(':')))


items = ['a', 'b', 'c']

result = ','.join(items)
print(result)


text = input()
delimiter = input()
# Write your code below
words_list = text.split()
output = delimiter.join(words_list) #delimiter.join(text.split())
print(output)