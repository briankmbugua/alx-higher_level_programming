#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[0:4]
word_last_2 = word[-2]
middle_word = word[(len(word)-1)//2:(len(word)+2)//2]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
