# fname = "test_input.txt";
fname = "input.txt"

with open(fname) as input_file:
    lines = [line.strip() for line in input_file]

print(lines)

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

shared = ""
i = 0
while not i >= len(lines):
    first = set(lines[i])
    second = set(lines[i+1])
    third = set(lines[i+2])
    print(first, second, third)

    badge = first.intersection(second).intersection(third)
    shared += "".join(badge)

    i += 3

print(shared)

sum_prio = 0
for char in shared:
    sum_prio += priority.find(char) + 1
    
print(sum_prio)

