sensors = []
beacons = []
dist = []
for line in open("day15/example.txt"):
    token = line.split()
    sensors.append([int(token[2][2:-1]), int(token[3][2:-1])])
    beacons.append([int(token[8][2:-1]), int(token[9][2:])])

for x in range(4000000):
    for y in range(4000000):
        for s, d in zip(sensors, dist):
            if abs(s[0] - x) + abs(s[1] - y) > dist

print("answer:", x * 4000000 + y)
