import sys
import heapq
from config import INF

class DijkstraQueue:
    def create_priority_queue(self, source_index):
        queue = []
        heapq.heappush(queue, (0, source_index))
        return queue

    def find_shortest_path(self, graph, source_index, destination_index):
        distances = []
        visitedNodes = []
        length = len(graph)
        counter = 0
        
        for i in range(length):
            distances.append(INF)
            visitedNodes.append(False)
        
        distances[source_index] = 0
        

        queue = self.create_priority_queue(source_index)

        while (len(queue) != 0):
            counter += 1
            evaNode = heapq.heappop(queue)
            visitedNodes.append(evaNode)
            evaNodeName = evaNode[1]
            #evaluate neighbours
            for i in range(1, length):
                if not visitedNodes[i]:
                    if graph[evaNodeName][i] != INF:
                        weight = graph[evaNodeName][i]
                        newWeight = weight + distances[evaNodeName]
                        if newWeight < distances[i]:
                            distances[i] = newWeight
                            heapq.heappush(queue, (newWeight, i))
        
            if visitedNodes[destination_index]:
                return distances[destination_index], counter

        return distances[destination_index], counter

    