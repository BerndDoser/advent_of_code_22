for line in open('day6/data.txt'):
    pos = 4
    for i in range(len(line) - 3):
        token = line.strip()[pos-4:pos]
        if (len(token) == len(set(token))): break
        pos += 1

    print("answer: ", pos)
