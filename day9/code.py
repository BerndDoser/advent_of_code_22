head = [0,0]
tail = [0,0]
positions = set()

for line in open('day9/data.txt'):
    direction, steps = line.split()
    for i in range(int(steps)):
        if direction == 'U': head[0] += 1
        if direction == 'D': head[0] -= 1
        if direction == 'R': head[1] += 1
        if direction == 'L': head[1] -= 1

        if abs(tail[0] - head[0]) == 2:
            tail[1] = head[1]
            if tail[0] > head[0]:
                tail[0] -= 1
            else:
                tail[0] += 1

        if abs(tail[1] - head[1]) == 2:
            tail[0] = head[0]
            if tail[1] > head[1]:
                tail[1] -= 1
            else:
                tail[1] += 1

        positions.add(tuple(tail))

print("answer part 1: ", len(positions))
