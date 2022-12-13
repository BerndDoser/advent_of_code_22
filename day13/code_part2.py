import ast
import functools

def order(list1, list2):
    for e1, e2 in zip(list1, list2):
        if isinstance(e1, int) and isinstance(e2, int):
            if e1 > e2:
                return -1
            if e1 < e2:
                return 1
            continue
        if isinstance(e1, int):
            e1 = [e1]
        if isinstance(e2, int):
            e2 = [e2]
        res = order(e1, e2)
        if res != 0:
            return res
    if len(list1) > len(list2):
        return -1
    if len(list1) < len(list2):
        return 1
    return 0

packets = [[[2]], [[6]]]
with open("day13/data.txt") as file:
    for line in file:
        if line.strip() == '':
            continue
        packets.append(ast.literal_eval(line.strip()))

packets.sort(key=functools.cmp_to_key(order), reverse=True)

print("answer part 2:", (packets.index([[2]])+1) * (packets.index([[6]])+1))
