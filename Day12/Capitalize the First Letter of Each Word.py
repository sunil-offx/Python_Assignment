def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

print(capitalize_words("python is fun"))  
