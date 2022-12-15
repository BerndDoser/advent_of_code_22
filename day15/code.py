sensors = []
beacons = []
for line in open("day15/data.txt"):
    token = line.split()
    sensors.append([int(token[2][2:-1]), int(token[3][2:-1])])
    beacons.append([int(token[8][2:-1]), int(token[9][2:])])

sy = 2000000
sx = set()

for s, b in zip(sensors, beacons):
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    dist_to_sy = abs(s[1] - sy)
    for i in range(dist - dist_to_sy + 1):
        sx.add(s[0] + i)
        sx.add(s[0] - i)
    # print(s, b, dist, dist_to_sy, sx)

for s in sensors:
    if s[1] == sy and s[0] in sx:
        sx.remove(s[0])

for b in beacons:
    if b[1] == sy and b[0] in sx:
        sx.remove(b[0])

print("answer:", len(sx))
