items = []
operation_type = []
operation_second = []
test_divisable = []
if_true = []
if_false = []

with open("day11/data.txt") as file:
    for line in file:
        if "Monkey" in line:
            line = next(file).strip()
            items.append(list(map(int, line.split(':')[1].split(','))))
            line = next(file).strip()
            operation = line.split('=')[1].strip().split()
            operation_type.append(operation[1])
            operation_second.append(operation[2])
            line = next(file).strip()
            test_divisable.append(int(line.split('by')[1].strip()))
            line = next(file).strip()
            if_true.append(int(line.split('monkey')[1].strip()))
            line = next(file).strip()
            if_false.append(int(line.split('monkey')[1].strip()))

from functools import reduce
lcm = reduce(lambda x, y: x*y, test_divisable)
inspect = [0] * len(items)
for r in range(10000):
    for monkey,_ in enumerate(items):
        for item in items[monkey]:
            inspect[monkey] += 1
            worry_index = 0
            if operation_type[monkey] == '*':
                if operation_second[monkey] == 'old':
                    worry_index = item * item
                else:
                    worry_index = item * int(operation_second[monkey])
            if operation_type[monkey] == '+':
                if operation_second[monkey] == 'old':
                    worry_index = item + item
                else:
                    worry_index = item + int(operation_second[monkey])
            # worry_index = int(worry_index / 3)
            worry_index %= lcm
            if worry_index % test_divisable[monkey]:
                items[if_false[monkey]].append(worry_index)
            else:
                items[if_true[monkey]].append(worry_index)
        items[monkey] = []

inspect.sort()
print("answer: ", (inspect[-1] * inspect[-2]))
