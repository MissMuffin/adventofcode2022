import numpy as np

fname = "day08/input_test.txt";
# fname = "day08/input.txt"

with open(fname) as input_file:
    test = [" ".join(list(line.strip())) for line in input_file]
    lines = np.genfromtxt(test, dtype=int)

# print(lines)

score_scenic  = 0
sum_visible  = 0
sum_visible = 2 * len(lines) + 2 * len(lines[0]) - 4

for y in range(1, len(lines)-1):
    for x in range(1, len(lines[y])-1):
        tree = lines[y][x]
        hori = lines[y,:]
        vert = lines[:,x]

        left = np.flip(hori[:x])
        right = hori[x+1:]
        top = np.flip(vert[:y])
        bot = vert[y+1:]

        if np.max(left) < tree or np.max(right) < tree or np.max(top) < tree or np.max(bot) < tree:
            sum_visible += 1
        
        dist_left = np.where(left>=tree)[0].flat[0] +1 if np.max(left) >= tree else len(left)
        dist_right = np.where(right>=tree)[0].flat[0] +1 if np.max(right) >= tree else len(right)
        dist_bot = np.where(bot>=tree)[0].flat[0] +1 if np.max(bot) >= tree else len(bot)
        dist_top = np.where(top>=tree)[0].flat[0] +1 if np.max(top) >= tree else len(top)

        score = dist_left * dist_right * dist_bot * dist_top
        if score > score_scenic:
            score_scenic = score

print(f"Number of visible trees: {sum_visible}")
print(f"Highest scenic score: {score_scenic}")
