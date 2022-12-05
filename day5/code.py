crates_str = []
moves = []
with open('day5/data.txt') as file:
    for line in file:
        crates_str.append(line.strip())
        if (line.strip() == ''): break

    for line in file:
        tokens = line.split()
        moves.append([int(tokens[1]), (int(tokens[3]) - 1), (int(tokens[5]) - 1)])

nb_stacks = int(crates_str[-2].split()[-1])
crates_str = crates_str[:-2]
crates_str.reverse()

crates = [''] * nb_stacks
for level in crates_str:
    for stack in range(nb_stacks):
        if (len(level)> 1 + 4 * stack):
            crates[stack] += level[1 + 4 * stack].strip()

for move in moves:
    (number, source, target) = tuple(move)
    # print(move, crates[source][-number:])
    crates[target] += crates[source][-number:][::-1]
    crates[source] = crates[source][:-number]
    # print(crates)

result = ''
for stack in crates:
    result += stack[-1]

print("answer: ", result)
