binary_1 = input("Input binary 1: ")
binary_2 = input("Input binary 2: ")

# AND operations
def binary_and(binary_1, binary_2):
    result = ""
    for i in range(len(binary_1)):
        if binary_1[i] == "1" and binary_2[i] == "1":
            result += "1"
        else:
            result += "0"
    return result

print("AND (&) operation:" , result := binary_and(binary_1, binary_2))

# Operasi Perkalian (*)
def binary_multiply(binary_1, binary_2):
    num1 = int(binary_1, 2)
    num2 = int(binary_2, 2)

    result = bin(num1 * num2)[2:]
    return result

print("Multiply (*) operation: " , result := binary_multiply(binary_1, binary_2))

# Operasi OR Bitwise (|)
def binary_or(binary_1, binary_2):
    result = ""
    for i in range(len(binary_1)):
        if binary_1[i] == "1" or binary_2[i] == "1":
            result += "1"
        else:
            result += "0"
    return result

print("OR (|) Operation:" , result := binary_or(binary_1, binary_2))

# Operasi +
def binary_add(binary_1, binary_2):
    num1 = int(binary_1, 2)
    num2 = int(binary_2, 2)

    result = bin(num1 + num2)[2:]
    return result

print("Add (+) operation: " , result := binary_add(binary_1, binary_2))

# Operasi rihgt shift (>>)
def binary_right_shift(binary, n):
    result = binary
    for _ in range(n):
        result = "0" + result[:-1]
    return result

print("Right shift operation: " , result := binary_right_shift(binary_2, 1))

# Operasi left shift (<<)
def binary_left_shift(binary, n):
    result = binary
    for _ in range(n):
        result = result[1:] + "0"
    return result

print("Left shift operation: " , result := binary_left_shift(binary_1, 1))
