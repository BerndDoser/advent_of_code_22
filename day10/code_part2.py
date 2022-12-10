register = 1
add_next = False
sum = 0
crt = []
crt_line = ['.'] * 40
crt_pos = 0
with open('day10/data.txt') as file:
    for cycle in range(1, 241):
        if crt_pos in [register-1, register, register+1]:
            crt_line[crt_pos] = "#"
        crt_pos += 1
        if cycle in [20, 60, 100, 140, 180, 220]:
            sum += cycle * register
        if cycle in [40, 80, 120, 160, 200, 240]:
            crt.append(crt_line)
            crt_line = ['.'] * 40
            crt_pos = 0
        if add_next:
            add_next = False
            register += add_value
        else:
            token = next(file).split()
            if token[0] == "addx":
                add_next = True
                add_value = int(token[1])

for line in crt:
    print("".join([str(i) for i in line]))
