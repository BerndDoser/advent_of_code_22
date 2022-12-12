import networkx as nx

map = []
for line in open('day12/data.txt'):
    map.append(line.strip())

nb_rows = len(map)
nb_cols = len(map[0])
nb_nodes = nb_rows * nb_cols

G = nx.DiGraph()

start = []
for i in range(nb_rows):
    for j in range(nb_cols):
        if map[i][j] == 'S':
            start.append(i * nb_cols + j)
            map[i] = map[i].replace('S', 'a')
        if map[i][j] == 'a':
            start.append(i * nb_cols + j)
        if map[i][j] == 'E':
            end = i * nb_cols + j
            map[i] = map[i].replace('E', 'z')

for i in range(nb_rows - 1):
    for j in range(nb_cols):
        diff = ord(map[i][j]) - ord(map[i+1][j])
        if diff < 2:
            G.add_edge((i+1) * nb_cols + j, i * nb_cols + j)
        if diff > -2:
            G.add_edge(i * nb_cols + j, (i+1) * nb_cols + j)

for i in range(nb_rows):
    for j in range(nb_cols - 1):
        diff = ord(map[i][j]) - ord(map[i][j+1])
        if diff < 2:
            G.add_edge(i * nb_cols + j+1, i * nb_cols + j)
        if diff > -2:
            G.add_edge(i * nb_cols + j, i * nb_cols + j+1)

length = []
for s in start:
    try:
        length.append(len(nx.dijkstra_path(G, s, end)) - 1)
    except Exception:
        pass

print("answer part 2:", min(length))
