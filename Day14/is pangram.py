import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print(is_pangram("The quick brown fox jumps over a lazy dog")) 
