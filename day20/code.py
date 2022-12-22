class circular_index:
    def __init__(self, len):
        self.len = len

    def pos(self, i):
        return (i + self.len) % self.len

code = []
for line in open('day20/data.txt'):
    code.append(int(line.strip()))

pos = [*range(len(code))]
ci = circular_index(len(code) + 1)

for i in range(len(code)):
    p = pos.index(i)
    move = code[p]
    if move > 0:
        move += 1
    if move < 0:
        move -= 1
    new_pos = ci.pos(p + move)
    if new_pos < p:
        code.insert(new_pos + 1, code[p])
        pos.insert(new_pos + 1, pos[p])
        del code[p + 1]
        del pos[p + 1]
    else:
        code.insert(new_pos, code[p])
        pos.insert(new_pos, pos[p])
        del code[p]
        del pos[p]

p0 = code.index(0)
ci = circular_index(len(code))
print("answer:",
      code[ci.pos(p0 + 1000)]
    + code[ci.pos(p0 + 2000)]
    + code[ci.pos(p0 + 3000)]
)
