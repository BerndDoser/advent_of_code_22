valves = {}
for line in open("day16/example.txt"):
    token = line.replace(',','').split()
    valves[token[1]]  = (int(token[4][5:-1]), token[9:])

print(valves)
print(valves['CC'][1])

released_pressure = 0
flow_rate = 0
current_valve = 'AA'
open = []
for i in range(30):
    mmax = 0
    for v in valves[current_valve][1]:
        if valves[v][0] > mmax:
            mmax = valves[v][0]
            next_valve = v
    released_pressure += flow_rate

print("answer:", released_pressure)
