### Напишете програма, която съкращава
# низ, като заменя повтарящите се
# символи с техния брой
# "aaabbccccd" -> "a3b2c4d1".

def compress_string(string):
    if not string:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            count += 1
        else:
            compressed.append(string[i - 1] + str(count))
            count = 1
    compressed.append(string[-1] + str(count))
    result = "".join(compressed)
    return result if len(result) < len(string) else string

text = input("Enter a string: ")
print("Original: ",text)
print("Compressed: ",compress_string(text))

