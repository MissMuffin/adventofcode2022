# https://adventofcode.com/2022/day/2

# fname = "input_test.txt";
fname = "input.txt"


with open(fname) as input_file:
    lines = [line.strip() for line in input_file]

# print(lines)

opp = [line[0] for line in lines]
me = [line[-1] for line in lines]

point_lookup_me = {"X":1, "Y":2, "Z":3}
point_lookup_opp = {"A":1, "B":2, "C":3}
me = [point_lookup_me[x] for x in me]
opp = [point_lookup_opp[x] for x in opp]

print(opp)
print(me)

points = 0
points += sum(me)

print(points)

for i,n in enumerate(opp):
    result = (n - me[i])%3
    # draw: 3 pts
    if result == 0:
        points += 3
    # win: 6 pts
    elif result == 2:
        points += 6

print(points)
