cubes = set()
for line in open('day18/data.txt'):
    cubes.add(tuple(map(int, line.strip().split(','))))

area = 0
for c in cubes:
    if not (c[0] + 1, c[1], c[2]) in cubes:
        area += 1
    if not (c[0], c[1] + 1, c[2]) in cubes:
        area += 1
    if not (c[0], c[1], c[2] + 1) in cubes:
        area += 1
    if not (c[0] - 1, c[1], c[2]) in cubes:
        area += 1
    if not (c[0], c[1] - 1, c[2]) in cubes:
        area += 1
    if not (c[0], c[1], c[2] - 1) in cubes:
        area += 1

print("answer:", area)
