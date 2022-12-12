calories = [0]
for line in open('day1/data.txt'):
    if line == '\n':
        calories.append(0)
        continue
    calories[-1] += int(line.strip())

print("answer part 1:", max(calories))

calories.sort()
print("answer part 2:", sum(calories[-3:]))
