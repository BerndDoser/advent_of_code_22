from itertools import cycle

for line in open("day17/data.txt"):
    jet_pattern = line.strip()
jets = [x for x in jet_pattern]

def get_rock(id, p):
    if id == 0:
        return [[2,p],[3,p],[4,p],[5,p]]
    elif id == 1:
        return [[3,p],[2,p+1],[3,p+1],[4,p+1],[3,p+2]]
    elif id == 2:
        return [[2,p],[3,p],[4,p],[4,p+1],[4,p+2]]
    elif id == 3:
        return [[2,p],[2,p+1],[2,p+2],[2,p+3]]
    elif id == 4:
        return [[2,p],[3,p],[2,p+1],[3,p+1]]

def push_right(rock, stack):
    for pos in rock:
        if pos[0] == 6:
            return
    rock_set = set((p[0]+1, p[1]) for p in rock)
    if len(rock_set.intersection(stack)) != 0:
        return
    for pos in rock:
        pos[0] += 1

def push_left(rock, stack):
    for pos in rock:
        if pos[0] == 0:
            return
    rock_set = set((p[0]-1, p[1]) for p in rock)
    if len(rock_set.intersection(stack)) != 0:
        return
    for pos in rock:
        pos[0] -= 1

def push_down(rock):
    for pos in rock:
        pos[1] -= 1

def draw(stack):
    for y in range(top, 0, -1):
        for x in range(7):
            if (x,y) in stack:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()

top = 0
jet_pool = cycle(jets)
stack = set((x,0) for x in range(7))
for i in range(2022):
    rock = get_rock(i%5, top + 4)
    falling = True
    while falling:
        if next(jet_pool) == '>':
            push_right(rock, stack)
        else:
            push_left(rock, stack)
        push_down(rock)
        rock_set = set(tuple(x) for x in rock)
        if len(rock_set.intersection(stack)) != 0:
            falling = False
            for pos in rock:
                stack.add((pos[0], pos[1] + 1))
            top = max(stack, key=lambda item:item[1])[1]

print("answer:", top)
