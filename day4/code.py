sum = 0
for line in open('day4/data.txt'):
    line = line.strip()
    ranges = line.split(',')
    r0 = list(map(int, ranges[0].split('-')))
    r1 = list(map(int, ranges[1].split('-')))
    if ((r0[0] <= r1[0] and r0[1] >= r1[1]) or
        (r1[0] <= r0[0] and r1[1] >= r0[1])):
        sum += 1

print("answer: ", sum)
