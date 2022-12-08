class Dir(object):

    def __init__(self, parent=None, children=[], name="/", size=0):
        self.parent = parent
        self.children = children
        self.name = name
        self.size = size

    def add_subdir(self, name, size=0):
        child = Dir(parent=self, name=name)
        child.children = []
        self.children.append(child)
        return child

    def add_file(self, size):
        self.size += size

    def __str__(self):
        res = ""
        res += f"{self.name} : {self.size}"
        return res

# fname = "day07/input_test.txt";
fname = "day07/input.txt"

with open(fname) as input_file:
    lines = [line.strip() for line in input_file]

# print(lines)

root = Dir()
curr_dir = root

for line in lines[1:]:
    if line[0] == "$":
        if line[2:4] == "cd":
            if line[-2:] == "..":
                curr_dir = curr_dir.parent
            else:
                curr_dir = curr_dir.add_subdir(name=line.split()[-1])
        elif line[2:4] == "ls":
            continue # ignore
    elif line[:3] == "dir":
        continue # ignore
    else:
        # is file
        size = int(line.split()[0])
        curr_dir.add_file(size)
    
def traverse(node, level=0, indent=2):
    if level > 0:
        prefixed_str = '|' * (indent * (level -1)) + '+-'
    else:
        prefixed_str = ''
    print(prefixed_str + str(node))
    for child in node.children:
        traverse(child, level=level+1)
# traverse(root)

def get_sizes(node):
    sum = node.size
    arr = []
    for child in node.children:
        childsum, childarr = get_sizes(child)
        sum += childsum
        arr += childarr
    arr += [sum]
    return sum, arr

sum, arr = get_sizes(root)
# print(arr)

arr = sorted(arr)

total = 0
options = []
for a in arr:
    if a < 100000:
        total += a
    if a >= (30000000 - (70000000 - arr[-1])):
        options.append(a)
options = sorted(options)

print(f"sum of total sizes of dirs < 100000: {total}")

print(f"used space: {arr[-1]}")
print(f"free space: {70000000 - arr[-1]}")
print(f"extra space needed: {30000000 - (70000000 - arr[-1])}")

print(f"best folder to delete: {options[0]}")
