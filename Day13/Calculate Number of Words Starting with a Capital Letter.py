def capital_word_count(s):
    return sum(1 for word in s.split() if word[0].isupper())

print(capital_word_count("Hello World, this Is Python"))  
