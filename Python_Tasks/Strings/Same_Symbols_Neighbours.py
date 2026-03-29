### Да се състави програма, която проверява
# дали зададен символен низ
# съдържа еднакви съседни символи.

def same_symbols_neighbours(string):
    if len(string) < 2:
        return False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return True
    return False

text = input("Write a text: ")
if same_symbols_neighbours(text):
    print("Yes")
else:
    print("No")
