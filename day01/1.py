# https://adventofcode.com/2022/day/1

with open("input.txt") as input_file:
    lines = [line.strip() for line in input_file]

cals = []
total = 0

# print(lines)

for food in lines:
    if food:
        total += int(food)
    else: 
        cals.append(total)
        total = 0

cals = sorted(cals)

# print(cals)

print(f"highest cals: {cals[-1]}", )
print(f"top 3 total cals: {cals[-1]+cals[-2]+cals[-3]}")
print(sum(cals[-3:]))

