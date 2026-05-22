text = "abcdeabc"
pattern = "abc"

for i in range(len(text)):
    if text[i:i + len(pattern)] == pattern:
        print(pattern)

    
