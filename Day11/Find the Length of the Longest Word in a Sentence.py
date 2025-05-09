def longest_word_length(sentence):
    words = sentence.split()
    return max(len(word) for word in words)

print(longest_word_length("Python is amazing"))  
