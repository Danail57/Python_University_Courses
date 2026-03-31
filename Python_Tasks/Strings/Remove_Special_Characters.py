### Write a program to remove special symbols
# and punctuation from a string

def remove_special_characters(string):
    result = ""
    for character in string:
        if character.isalnum() or character == " ":
            result += character
    return result
text = input("Write a text: ")
cleaned_text = remove_special_characters(text)
print(cleaned_text)
