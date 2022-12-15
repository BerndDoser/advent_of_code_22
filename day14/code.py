import sys

rocks = []
lower = [sys.maxsize, 0]
upper = [0, 0]
for line in open("day14/data.txt"):
    line = line.strip().split('->')
    one_rock = []
    for coord in line:
        coord = list(map(int, coord.strip().split(',')))
        lower[0] = min(lower[0], coord[0])
        lower[1] = min(lower[1], coord[1])
        upper[0] = max(upper[0], coord[0])
        upper[1] = max(upper[1], coord[1])
        one_rock.append(coord)
    rocks.append(one_rock)

dim = [m - n + 1 for m,n in zip(upper, lower)]
scan = set()
x_min = lower[0]

for rock in rocks:
    for i in range(len(rock) - 1):
        print(rock[i], rock[i+1])
        for j in range(min(rock[i][0], rock[i+1][0]), max(rock[i][0], rock[i+1][0]) + 1):
            scan.add((j, rock[i][1]))
        for j in range(min(rock[i][1], rock[i+1][1]), max(rock[i][1], rock[i+1][1]) + 1):
            scan.add((rock[i][0], j))

cycle = 0
overflow = False
sand = set()
while not overflow:
    x = 500
    for y in range(dim[1] + 2):
        if y == dim[1] + 1:
            overflow = True
            break
        if (x, y+1) in scan.union(sand):
            if not (x-1, y+1) in scan.union(sand):
                x -= 1
            elif not (x+1, y+1) in scan.union(sand):
                x += 1
            else:
                sand.add((x,y))
                break
    if not overflow:
        cycle += 1

for y in range(dim[1]):
    for x in range(dim[0]):
        if (x + x_min, y) in scan:
            print("#", end='')
        elif (x + x_min, y) in sand:
            print('o', end='')
        else:
            print(".", end='')
    print('')

print('answer:', cycle)
