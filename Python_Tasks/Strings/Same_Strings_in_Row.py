### Зададен е двумерният масив от символни
# низове А с m реда n стълба.
# Да се състави програма, която проверява дали има ред,
# съдържащ два еднакви низа.

def check_rows_with_sets(matrix):
    found_duplicate = False
    for i, row in enumerate(matrix):
        if len(set(row)) < len(row):
            #set(row) deletes the duplicates
            print(f"{i + 1}: {set(row)}")
            found_duplicate = True
        else:
            print(f"Row {i + 1}: no duplicates")
    return found_duplicate

m = int(input("Rows: "))
n = int(input("Columns: "))
matrix = []
for i in range(m):
    print(f"Row {i + 1}: ")
    current_row = []
    for j in range(n):
        element = input(f"Write a string for position [{i + 1}][{j + 1}]: ")
        current_row.append(element)
    matrix.append(current_row)
print("Results: ")
check_rows_with_sets(matrix)
