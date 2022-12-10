import re
import itertools

# fname = "input_test.txt";
fname = "input.txt"

stacks_padded = []
instructions = []

with open(fname) as input_file:
    is_stack = True
    for line in input_file:
        if line is "\n":
            is_stack = False
        else:
            if is_stack:
                stacks_padded.append(re.findall("\w", line.replace("    ", "0")))
            else:
                instructions.append(re.findall("\d+", line))

# print(stacks)
print(instructions)

# transpose stacks so that on element in list is one stack
# discards no data if jagged and fills short nested lists with None
stacks_padded = list(map(list, itertools.zip_longest(*reversed(stacks_padded[:-1]), fillvalue=None)))
# print(stacks)

# remove empty containers at the end of each stack
stacks = []
for stack in stacks_padded:
    stacks.append([c for c in stack if c != "0"])

print(stacks)

# do instructions
for ins in instructions:
    c, movf, movt = int(ins[0]), int(ins[1])-1, int(ins[2])-1
    moved = stacks[movf][-c:]
    cutoff = len(stacks[movf]) - c
    stacks[movf] = stacks[movf][:cutoff]
    stacks[movt] += moved
    print(stacks)

# get result string
res = ""
for stack in stacks:
    res += stack[-1]
print(res)