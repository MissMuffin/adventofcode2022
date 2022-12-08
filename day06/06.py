import re

# fname = "input_test.txt";
fname = "input.txt"

with open(fname) as input_file:
    lines = input_file.read()

# print(lines)

def has_no_repeating_chars(x):
    return len(set(x)) == len(x)

for i, char in enumerate(lines):
    if i > len(lines) - 14:
        break

    ident = lines[i:i+14]
    # print(ident)
    
    if has_no_repeating_chars(ident):
        print(i + 14)
        break