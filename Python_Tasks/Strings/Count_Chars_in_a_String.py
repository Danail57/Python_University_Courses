### Зададен е едномерният масив от символни низове
# А0, А1,...,Аn-1. Да се състави програма, която калкулира
# колко пъти се среща зададен символ в низа Аi.

def count_chars_in_string(target_string, char_to_find):
    if not target_string:
        return 0
    count = 0
    for char in target_string:
        if char == char_to_find:
            count += 1
    return count

def user_input():
    try:
        n = int(input("Total elements: "))
        matrix = []
        for i in range(n):
            matrix.append(input(f"Enter the element {i + 1}: "))

        index = int(input("Enter the index of the element you want to enter: "))
        symbol = input("Enter the symbol to count: ")
        if 0 <= index < len(matrix):
            target = matrix[index]
            result = count_chars_in_string(target, symbol)

            print(f"\nResult: Symbol '{symbol}' is found {result} times in '{target}'.")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid index.")
user_input()
