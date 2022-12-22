def get(data, item):
    token = data[item].split()
    if len(token) == 1:
        return int(token[0])
    else:
        a = get(data, token[0])
        op = token[1]
        b = get(data, token[2])
        if op == '+':
            return int(a + b)
        if op == '-':
            return int(a - b)
        if op == '*':
            return int(a * b)
        if op == '/':
            return int(a / b)

data = {}
for line in open("day21/data.txt"):
    token = line.strip().split(':')
    data[token[0]] = token[1].strip()

print(data)
root = get(data, "root")

print("answer:", root)
