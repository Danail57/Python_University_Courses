### Write a program to count occurrences
# of all characters within a string

from collections import Counter

def count_occurences(string):
    return Counter(string)

text = input("Write a text: ")
print(count_occurences(text))
