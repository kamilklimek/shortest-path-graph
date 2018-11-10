import sys
INFINITE = sys.maxint

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph
        self.length = len(graph)
    
    def get_min_distance_vertex_index(self, distances, visits, counter):
        min = INFINITE

        for vertex_index in range(0, len(distances)):
            counter += 1
            if visits[vertex_index] == False and distances[vertex_index] <= min:
                min = distances[vertex_index]
                min_index = vertex_index

        return min_index

    def find_shortest_path(self, source_index, destination_index):
        distances = []
        visits = []
        counter = 0

        for index in range(0, len(self.graph)):
            distances.append(INFINITE)
            visits.append(False)

        distances[source_index] = 0

        for index in range(len(self.graph)):
            
            min_distance_vertex_index = self.get_min_distance_vertex_index(distances, visits, counter)
            visits[min_distance_vertex_index] = True

            for inner_index in range(len(self.graph)):
                counter += 1
                node_not_visited = visits[inner_index] == False
                is_not_the_same_node = self.graph[min_distance_vertex_index][inner_index] != 0
                distance_is_not_infinite = distances[min_distance_vertex_index] != INFINITE
                is_the_shortest_way = distances[min_distance_vertex_index] + self.graph[min_distance_vertex_index][inner_index] < distances[inner_index]


                if node_not_visited and is_not_the_same_node and distance_is_not_infinite and is_the_shortest_way:
                    distances[inner_index] = distances[min_distance_vertex_index] + self.graph[min_distance_vertex_index][inner_index]

            #if distances[destination_index] != INFINITE:
            #    return (distances[destination_index], counter)
        
        return (distances, counter)

    