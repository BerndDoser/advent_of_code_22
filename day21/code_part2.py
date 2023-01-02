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

def find_humn(data, item):
    token = data[item].split()
    if len(token) == 1:
        return False
    elif 'humn' in token:
        return True
    else:
        return find_humn(data, token[0]) or find_humn(data, token[2])

data = {}
for line in open("day21/example.txt"):
    token = line.strip().split(':')
    data[token[0]] = token[1].strip()

root = data['root'].split()
if find_humn(data, root[0]):
    value = get(data, root[1])
    token = data[root[0]].split()
        if find_humn(data, token[0]):
    

root = get(data, "root")

print("answer:", root)
