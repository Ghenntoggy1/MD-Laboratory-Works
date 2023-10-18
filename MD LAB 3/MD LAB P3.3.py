# 3.3 Let's do ratings
import json
import pprint


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist, l):
        # print("Vertex \t Distance from Source")
        for node in range(self.V):
            l.append(dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
        # Initialize minimum distance for next node
        min = 1e7
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src, l):
        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        for cout in range(self.V):
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                        sptSet[v] == False and
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist, l)


matrix = []
with open('matrix.txt') as f:
    t = f.read()
    for i in t:
        if i.isdigit():
            matrix.append(int(i))
f.close()
with open('matrix.txt') as f:
    lines = f.readline().strip('\n')
    names = lines.split(" | ")
    names[0] = 'Caleb Hobby'
f.close()
matrix2 = []
for i in range(0, len(matrix), 20):
    matrix2.append(matrix[i:i + 20])

g = Graph(20)
g.graph = matrix2

matrixSPT = []
for i in range(20):
    matrixSPT.append(g.dijkstra(i, matrixSPT))

matrixSPT2 = []
for i in matrixSPT:
    if i is None:
        matrixSPT.remove(i)

for i in range(0, len(matrixSPT), 20):
    matrixSPT2.append(matrixSPT[i:i + 20])

rating = []
for i in matrixSPT2:
    r = 0
    for j in i:
        r += j
    rating.append(r)

dict = dict(zip(names, rating))

for idx, (k, v) in enumerate(dict.items()):
    print(k, "-", v)

with open('matrixSPT3-3.txt', 'w') as txt:
    for line in matrixSPT2:
        txt.write("".join(str(line)[1:-1]) + "\n")
txt.close()
