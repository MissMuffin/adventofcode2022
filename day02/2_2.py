# https://adventofcode.com/2022/day/2

# fname = "input_test.txt";
fname = "input.txt"


with open(fname) as input_file:
    lines = [line.strip() for line in input_file]

# print(lines)

outcome = [line[-1] for line in lines]
opp = [line[0] for line in lines]

point_lookup_outcome = {"X":0, "Y":3, "Z":6}
point_lookup_opp = {"A":1, "B":2, "C":3}
outcome = [point_lookup_outcome[x] for x in outcome]
opp = [point_lookup_opp[x] for x in opp]

print(opp)
print(outcome)

logic = [
    {"6":2, "0":3, "3":1},
    {"6":3, "0":1, "3":2},
    {"6":1, "0":2, "3":3}
]

moves = []

for i,n in enumerate(opp):
    moves.append(logic[n-1].get(str(outcome[i])))

print(moves)

points = sum(moves) + sum(outcome)
print(points)
