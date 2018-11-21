from dijsktra_find_max import Dijkstra
from bellmanFord import BellmanForda
from dijkstra_prio_que import DijkstraQueue
from converted_graph import convert_graph_from_value_to_value
from graph_generator import generate_graph
import timeit
import sys
from config import INF
from termcolor import colored

tests_graph = []

tests_graph.append(
    (
        (0, 6, 9),
        [
            [0, 3, 2, 5, 0, 7, 0],
            [3, 0, 0, 1, 5, 0, 0],
            [2, 0, 0, 1, 0, 8, 0],
            [5, 1, 1, 0, 3, 0, 0],
            [0, 5, 0, 3, 0, 0, 0],
            [7, 0, 8, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 2, 0],
        ]
    )
)

tests_graph.append(
    (
        (0, 2, 7),
        [
            [0, 1, 0, 1, 0],
            [1, 0, 0, 0, 2],
            [0, 0, 0, 0, 4],
            [1, 0, 0, 0, 3],
            [0, 2, 4, 3, 0],
        ]
    )
)

tests_graph.append(
    (
        (2, 1, 10),
        [
            [0, 0, 0, 6, 2],
            [0, 0, 0, 2, 1],
            [0, 0, 0, 8, 0],
            [6, 2, 8, 0, 0],
            [2, 1, 0, 0, 0],
        ]
    )
)

dijkstra_priority_queue = DijkstraQueue()
bellmanFord = BellmanForda()
dijkstra = Dijkstra()



graph_number = 1
for test in tests_graph:
    (data, graph) = test
    (source, destination, expectedValue) = data

    start = timeit.default_timer()
    result = dijkstra.find_shortest_path(graph, source, destination)
    end = timeit.default_timer()
    value, amount_operation = result


    print("============= GRAPH - "  + str(graph_number) + " ==========================");
    if expectedValue == value:
        print("\033[1;32;40m \n")
    else:
        print("\033[1;31;42m \n")    
    


    print("*********** DIJKSTRA MAX *************")
    print("Oczekiwana wartosc: " + str(expectedValue))
    print("Rzeczywista wartosc: " + str(value))
    print("Liczba operacji: " + str(amount_operation))
    print("Czas: " + str(end-start))
    print("Test zdany: " + str( expectedValue == value))

    converted_graph = convert_graph_from_value_to_value(graph, 0, INF)


    start = timeit.default_timer()
    result = dijkstra_priority_queue.find_shortest_path(converted_graph, source, destination)
    end = timeit.default_timer()

    value, amount_operation = result
    if expectedValue == value:
        print("\033[1;32;40m \n")
    else:
        print("\033[1;31;42m \n")  
    

    print("*********** DIJKSTRA PRIORITY QUEUE *************")
    print("Oczekiwana wartosc: " + str(expectedValue))
    print("Rzeczywista wartosc: " + str(value))
    print("Liczba operacji: " + str(amount_operation))
    print("Czas: " + str(end-start))
    print("Test zdany: " + str( expectedValue == value))

    start = timeit.default_timer()
    result = bellmanFord.find_shortest_path(converted_graph, source, destination)
    end = timeit.default_timer()

    value, amount_operation = result
    if expectedValue == value:
        print("\033[1;32;40m \n")
    else:
        print("\033[1;31;42m \n")  
    


    print("*********** BELLMAN FORD *************")
    print("Oczekiwana wartosc: " + str(expectedValue))
    print("Rzeczywista wartosc: " + str(value))
    print("Liczba operacji: " + str(amount_operation))
    print("Czas: " + str(end-start))
    print("Test zdany: " + str( expectedValue == value))
    graph_number += 1

