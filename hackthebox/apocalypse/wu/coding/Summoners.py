# Input the text as a single string
input_text = input()  # Example: "[3, 2, 5, 10, 7]"

# Write your solution below
import ast

def max_non_adjacent_sum(tokens):
    if not tokens:
        return 0
    if len(tokens) == 1:
        return tokens[0]

    include = 0
    exclude = 0

    for energy in tokens:
        new_exclude = max(include, exclude)  # Jika tidak mengambil elemen saat ini
        include = exclude + energy  # Jika mengambil elemen saat ini
        exclude = new_exclude  # Perbarui exclude

    return max(include, exclude)

# Convert input string to list
tokens = ast.literal_eval(input_text)

# Output the result
print(max_non_adjacent_sum(tokens))