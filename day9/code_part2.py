knots = [[0,0] for i in range(10)]
positions = set()

for line in open('day9/data.txt'):
    direction, steps = line.split()
    for i in range(int(steps)):
        if   direction == 'U': knots[0][0] += 1
        elif direction == 'D': knots[0][0] -= 1
        elif direction == 'R': knots[0][1] += 1
        elif direction == 'L': knots[0][1] -= 1

        for i in range(1,10):
            if (abs(knots[i][0] - knots[i-1][0]) == 2) and (abs(knots[i][1] - knots[i-1][1]) == 2):
                if knots[i][0] > knots[i-1][0]:
                    knots[i][0] -= 1
                else:
                    knots[i][0] += 1
                if knots[i][1] > knots[i-1][1]:
                    knots[i][1] -= 1
                else:
                    knots[i][1] += 1

            elif abs(knots[i][0] - knots[i-1][0]) == 2:
                knots[i][1] = knots[i-1][1]
                if knots[i][0] > knots[i-1][0]:
                    knots[i][0] -= 1
                else:
                    knots[i][0] += 1

            elif abs(knots[i][1] - knots[i-1][1]) == 2:
                knots[i][0] = knots[i-1][0]
                if knots[i][1] > knots[i-1][1]:
                    knots[i][1] -= 1
                else:
                    knots[i][1] += 1

        positions.add(tuple(knots[9]))

print("answer part 2: ", len(positions))
