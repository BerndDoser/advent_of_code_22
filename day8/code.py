trees = []
for line in open('day8/data.txt'):
    line = line.strip()
    row = []
    for i in line:
        row.append(int(i))
    trees.append(row)

assert(len(trees) == len(trees[0]))

LENGTH = len(trees)
vis = [[0 for x in range(LENGTH)] for y in range(LENGTH)]
for i in range(0, LENGTH):
    vis[i][0] = 1
    vis[i][LENGTH - 1] = 1
    vis[0][i] = 1
    vis[LENGTH - 1][i] = 1

for i in range(1, LENGTH - 1):
    largest = trees[i][0]
    for j in range(1, LENGTH - 1):
        if trees[i][j] > largest:
            vis[i][j] = 1
            largest = trees[i][j]

for j in range(1, LENGTH - 1):
    largest = trees[0][j]
    for i in range(1, LENGTH - 1):
        if trees[i][j] > largest:
            vis[i][j] = 1
            largest = trees[i][j]

for i in range(1, LENGTH - 1):
    largest = trees[i][LENGTH - 1]
    for j in range(LENGTH - 2, 0, -1):
        if trees[i][j] > largest:
            vis[i][j] = 1
            largest = trees[i][j]

for j in range(1, LENGTH - 1):
    largest = trees[LENGTH - 1][j]
    for i in range(LENGTH - 2, 0, -1):
        if trees[i][j] > largest:
            vis[i][j] = 1
            largest = trees[i][j]

visible = sum(sum(vis,[]))
print("answer part 1: ", visible)

scenic_score = [[0 for x in range(LENGTH)] for y in range(LENGTH)]
for i in range(1, LENGTH - 1):
    for j in range(1, LENGTH - 1):

        height = trees[i][j]

        FACTOR = 0
        for left in range(j-1, -1, -1):
            FACTOR += 1
            if trees[i][left] >= height: break

        scenic_score[i][j] = FACTOR

        FACTOR = 0
        for right in range(j+1, LENGTH):
            FACTOR += 1
            if trees[i][right] >= height: break

        scenic_score[i][j] *= FACTOR

        FACTOR = 0
        for up in range(i-1, -1, -1):
            FACTOR += 1
            if trees[up][j] >= height: break

        scenic_score[i][j] *= FACTOR

        FACTOR = 0
        for down in range(i+1, LENGTH):
            FACTOR += 1
            if trees[down][j] >= height: break

        scenic_score[i][j] *= FACTOR

print("answer part 2: ", max(sum(scenic_score, [])))
