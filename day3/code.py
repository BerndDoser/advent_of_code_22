sum = 0
for line in open('day3/data.txt'):
    line = line.strip()
    half = int(len(line) / 2)
    item = list(set(line[0:half]).intersection(line[half:len(line)]))[0]
    if item.isupper():
        priority = ord(item) - 38
    else:
        priority = ord(item) - 96
    sum += priority

print("answer: ", sum)
