### Write a program to split a given string
# on hyphens and display each substring.

def split_string(string):
    return string.split("-")

sentence = input("Write a sentence with hyphens: ")
split_sentence = split_string(sentence)
for part in split_sentence:
    print(part)
