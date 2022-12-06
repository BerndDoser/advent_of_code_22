nb_distinct_chars = 14
for line in open('day6/data.txt'):
    pos = nb_distinct_chars
    for i in range(len(line) - nb_distinct_chars + 1):
        token = line.strip()[pos - nb_distinct_chars:pos]
        if (len(token) == len(set(token))): break
        pos += 1

    print("answer: ", pos)
