import numpy as np

data = np.loadtxt('day2/data.txt', dtype=str)
score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

choose = [[3, 1, 2], # lose
          [1, 2, 3], # draw
          [2, 3, 1]] # win

result = 0
for round in data:
    s0 = score[round[0]]
    s1 = score[round[1]]
    c = choose[s1 - 1][s0 - 1]
    result += c
    if s1 == 2: result += 3
    if s1 == 3: result += 6

print("answer part 2: ", result)
