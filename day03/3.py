# fname = "test_input.txt";
fname = "input.txt"

with open(fname) as input_file:
    lines = [line.strip() for line in input_file]

print(lines)

priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

shared = ""
for line in lines:
    first = line[0:int(len(line)/2)]
    second = line[int(len(line)/2):]
    print(first, second)

    print(set(first).intersection(set(second)))
    shared += "".join(set(first).intersection(set(second)))

print(shared)

sum_prio = 0
for char in shared:
    sum_prio += priority.find(char) + 1
    
print(sum_prio)

