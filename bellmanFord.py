import sys

INFINITE = -sys.maxint-1

class BellmanForda:
    def __init__(self, graph):
        self.graph=graph
        self.length=len(graph)

    def find_shortest_path(self, source, destination):
        distances = []
        poprzednik = []

        for i in range(self.length):
            distances.append(INFINITE)
            poprzednik.append(-1)

        distances[source] = 0

        for i in range(1, self.length):
            for j in range(self.length):
                edge_exist = self.graph[1][j] != 0
                temp_distance = distances[i] + self.graph[j][i]

                if edge_exist and distances[j] > temp_distance:
                    distances[j] = temp_distance
                    poprzednik[j] = i
            
        return (distances, poprzednik)