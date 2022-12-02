import numpy as np

data = np.loadtxt('day2/data.txt', dtype=str)
score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}

def won(s1, s2):
    if s1 == 3 and s2 == 1: return True
    if s1 == 1 and s2 == 2: return True
    if s1 == 2 and s2 == 3: return True
    return False

result = 0
for round in data:
    s0 = score[round[0]]
    s1 = score[round[1]]
    result += s1
    if s0 == s1: result += 3
    if won(s0, s1): result += 6

print("answer part 1: ", result)
