### Напишете програма, която разпъва
# низ:  "a3b2c4d1" -> "aaabbccccd".

def decompress_string(string):
    result = ""
    i = 0

    while i < len(string):
        char = string[i]
        i += 1
        number_str = ""

        while i < len(string) and string[i].isdigit():
            number_str += string[i]
            i += 1
        result += char * int(number_str)
    return result
compressed_text = input("Enter a string: (for example: a3v5d9): ")
print("Original string:", decompress_string(compressed_text))
