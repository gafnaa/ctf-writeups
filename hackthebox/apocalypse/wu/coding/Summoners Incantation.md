# Summoners Incantation

## Desc
To awaken the ancient power of the Dragon's Heart, the summoners must combine magical incantation tokens. However, the tokens are delicate; no two adjacent tokens can be combined without losing their energy. The optimal incantation is the maximum sum obtainable by choosing non-adjacent tokens.

## Solution

```py
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
```

## Flag
    HTB{SUMM0N3RS_INC4NT4T10N_R3S0LV3D_02779f00f64db320b149988f9bf0c0aa}