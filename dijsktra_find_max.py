import sys
from config import INF

class Dijkstra:    
    def get_min_distance_vertex_index(self, distances, visits, counter):
        min = INF
        for vertex_index in range(0, len(distances)):
            counter[0] += 1
            if visits[vertex_index] == False and distances[vertex_index] <= min:
                min = distances[vertex_index]
                min_index = vertex_index

        return min_index

    def find_shortest_path(self, graph, source_index, destination_index):
        distances = []
        visits = []
        counter = 0

        length = len(graph)

        for index in range(length):
            distances.append(INF)
            visits.append(False)

        distances[source_index] = 0

        for index in range(length):
            #find min_weight            
            min = INF
            for vertex_index in range(0, len(distances)):
                counter += 1
                if visits[vertex_index] == False and distances[vertex_index] <= min:
                    min = distances[vertex_index]
                    min_distance_vertex_index = vertex_index

            visits[min_distance_vertex_index] = True

            for inner_index in range(length):
                counter += 1
                node_not_visited = visits[inner_index] == False
                is_not_the_same_node = graph[min_distance_vertex_index][inner_index] != 0
                distance_is_not_infinite = distances[min_distance_vertex_index] != INF
                is_the_shortest_way = distances[min_distance_vertex_index] + graph[min_distance_vertex_index][inner_index] < distances[inner_index]


                if node_not_visited and is_not_the_same_node and distance_is_not_infinite and is_the_shortest_way:
                    distances[inner_index] = distances[min_distance_vertex_index] + graph[min_distance_vertex_index][inner_index]

        if visits[destination_index] == True:
            return (distances[destination_index], counter)

        
        return (distances[destination_index], counter)

    