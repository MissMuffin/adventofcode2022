# fname = "input_test.txt";
fname = "input.txt"

with open(fname) as input_file:
    lines = [line.strip().split(',') for line in input_file]

# print(lines)

full_overlap = 0
partial_overlap = 0

for pair in lines:
    ranges = [range.split("-") for range in pair]
    # print(ranges)

    beg_first = int(ranges[0][0])
    end_first = int(ranges[0][1])
    beg_sec = int(ranges[1][0])
    end_sec = int(ranges[1][1])

    if  beg_first >= beg_sec and beg_first <= end_sec:
        if end_first <= end_sec:
            full_overlap += 1
            # print("full")
        else:
            partial_overlap += 1
            # print("partial")

    elif beg_sec >= beg_first and beg_sec <= end_first:
        if end_sec <= end_first:
            full_overlap += 1
            # print("full")
        else:
            partial_overlap += 1
            # print("partial")

print(f"full overlap: {full_overlap}")
print(f"partial overlap: {partial_overlap}")

print(full_overlap + partial_overlap)
