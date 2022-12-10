from readline import append_history_file


# fname = "day10/input_test.txt";
fname = "day10/inpjfut.txt"

with open(fname) as input_file:
    lines  = [line.strip().split() for line in input_file]

# print(lines)

cycles = []
x = 1
buffer = None
instr = lines

while len(instr) > 0:
    
    if buffer:
        cycles.append(x)
        x += int(buffer[1])
        buffer = None
        continue
    
    buffer = instr.pop(0)
    if buffer[0] == "noop":
        buffer = None
        
    cycles.append(x)

if buffer != None:
    cycles.append(x)
    x += int(buffer[1])
    cycles.append(x)

# print(cycles)

c20 = cycles[20-1]
c60 = cycles[60-1]
c100 = cycles[100-1]
c140 = cycles[140-1]
c180 = cycles[180-1]
c220 = cycles[220-1]

print(f"20th  : {c20} = {c20 * 20}")
print(f"60th  : {c60} = {c60 * 60}")
print(f"100th : {c100} = {c100 * 100}")
print(f"140th : {c140} = {c140 * 140}")
print(f"180th : {c180} = {c180 * 180}")
print(f"220th : {c220} = {c220 * 220}")
print(f"total sum: {c20 * 20 + c60 * 60 + c100 * 100 + c140 * 140 + c180 * 180 + c220 * 220}")

screen = ""
for cycle, pos in enumerate(cycles):
    if (cycle % 40) in [pos-1, pos, pos+1]:
        screen += "#"
    else:
        screen += "."

for i in range(0, len(screen), 40):
    print(screen[i:i+40])