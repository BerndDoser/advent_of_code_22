import ast

def order(list1, list2):
    # print(list1, " ... ", list2)
    for e1, e2 in zip(list1, list2):
        # print(e1, " .. ", e2)
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

res = 0
idx = 0
with open("day13/data.txt") as file:
    for line in file:
        if line.strip() == '':
            continue
        idx += 1
        # print(idx)
        list1 = ast.literal_eval(line.strip())
        list2 = ast.literal_eval(next(file).strip())
        if order(list1, list2) == 1:
            # print("right order")
            res += idx

print("answer:", res)
