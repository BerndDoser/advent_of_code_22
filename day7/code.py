pwd = ['/']
dirs = {}
dirs['/'] = 0
with open('day7/data.txt') as file:
    for line in file:
        line = line.strip()
        if line == '$ ls' or line == '$ cd /' or 'dir' in line:
            continue
        elif line == '$ cd ..':
            pwd.pop()
        elif '$ cd' in line:
            pwd.append(line.split()[2])
            dirs['/'.join(pwd)] = 0
        else:
            dirs['/'.join(pwd)] += int(line.split()[0])
            for i in range(1, len(pwd)):
                dirs['/'.join(pwd[:-i])] += int(line.split()[0])

size = 0
for s in dirs.values():
    if s <= 100000: size += s

print("answer part 1: ", size)

smallest = dirs['/']
needed_space = abs(70000000 - dirs['/'] - 30000000)

for s in dirs.values():
    if s < smallest and s > needed_space: smallest = s

print("answer part 2: ", smallest)
