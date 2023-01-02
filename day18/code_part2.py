cubes = set()
for line in open('day18/example.txt'):
    cubes.add(tuple(map(int, line.strip().split(','))))

min_ = [min(cubes, key=lambda item:item[x])[x] for x in range(3)]
max_ = [max(cubes, key=lambda item:item[x])[x] for x in range(3)]
print(min_, max_)

water = set()
for x in range(max_[0]):
    for y in range(max_[1]):
        water.add((x,y,min_[2]))
        water.add((x,y,max_[2]))

print('water:', water)

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
