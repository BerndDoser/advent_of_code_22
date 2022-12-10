register = 1
add_next = False
sum = 0
with open('day10/data.txt') as file:
    for cycle in range(1, 221):
        # print(cycle, register)
        if cycle in [20, 60, 100, 140, 180, 220]:
            # print(cycle, register)
            sum += cycle * register
        if add_next:
            add_next = False
            register += add_value
        else:
            token = next(file).split()
            # print(token)
            if token[0] == "addx":
                add_next = True
                add_value = int(token[1])

print("answer: ", sum)
