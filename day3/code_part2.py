sum = 0
file = open('day3/data.txt')
for line in file:
    line = line.strip()
    item = list(set(line).intersection(next(file)).intersection(next(file)))[0]
    if item.isupper():
        priority = ord(item) - 38
    else:
        priority = ord(item) - 96
    sum += priority

print("answer: ", sum)
