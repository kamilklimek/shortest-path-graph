from config import INF
class Edge:
    def __init__(self, fr, to, weight):
        self.weight=weight
        self.fr=fr
        self.to=to

    def __str__(self):
        return "Weight: " + str(self.weight) + ", from: " + str(self.fr) + ", to: " + str(self.to);

class Vertex:
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

class BellmanForda:
    def getEdgesByArray(self, graph):
        vertex = []
        for i in range(len(graph)):
            edges = []
            for j in range(len(graph[i])):
                if graph[i][j] == 0x90:
                    continue
                edges.append(Edge(i, j, graph[i][j]))
            vertex.append(Vertex(i, edges))
        return vertex

    def find_shortest_path(self, graph, source, destination):
        distances = []
        poprzednik = []
        counter = 0
        length = len(graph)
        vertex= self.getEdgesByArray(graph)

        for i in range(length):
            distances.append(INF)
            poprzednik.append(-1)

        distances[source] = 0

        for i in range(length):
            for edge in vertex[i].edges:
                counter += 1
                relax_condition = distances[edge.to] > distances[edge.fr] + edge.weight
                if relax_condition:
                    distances[edge.to] = distances[edge.fr] + edge.weight
                    poprzednik[edge.to] = edge.to

        return (distances[destination], counter)