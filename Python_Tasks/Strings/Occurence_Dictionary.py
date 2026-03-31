### Write a program to count occurrences
# of all characters within a string

def count_occurences(string):
    counts = {}
    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts
text = input("Write a string: ")
print(count_occurences(text))
