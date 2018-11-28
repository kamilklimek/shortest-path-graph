from dijsktra_find_max import Dijkstra
from bellmanFord import BellmanForda
from dijkstra_prio_que import DijkstraQueue
from converted_graph import convert_graph_from_value_to_value
import timeit
from config import INF

def load_graph(file_name, amount_nodes):
    file_handler = open('tests/' + file_name, 'r')
    graph = [ [ None ] * amount_nodes ] * amount_nodes 

    for row_index in range(amount_nodes):
        line = file_handler.readline().split(' ')
        for col_index in range(amount_nodes):
            graph[row_index][col_index] = int(line[col_index])
        
    return graph


def load_test_meta(file_name):
    file_handler = open(file_name, 'r')
    lines = file_handler.readlines()
    return [line.strip() for line in lines]

def get_tuples_by_file_name(file_names):
    values = [line.split(':') for line in file_names]
    return [(value[0], int(value[1])) for value in values]

def run_test(graph):
    dijkstra_priority_queue = DijkstraQueue()
    bellmanFord = BellmanForda()
    dijkstra = Dijkstra()
    destination = int(len(graph) / 2)

    converted_graph = convert_graph_from_value_to_value(graph, 0, INF)


    start = timeit.default_timer()
    dijkstra_result = dijkstra.find_shortest_path(graph, 0, destination)
    end = timeit.default_timer()

    dijkstra_time = end-start

    start = timeit.default_timer()
    dijkstra_prio_que_result = dijkstra_priority_queue.find_shortest_path(converted_graph, 0, destination)
    end = timeit.default_timer()

    dijkstra_prio_que_time = end-start

    start = timeit.default_timer()
    bellman_ford_result = bellmanFord.find_shortest_path(converted_graph, 0, destination)
    end = timeit.default_timer()

    bellman_ford_time = end-start

    return (dijkstra_result, dijkstra_time), (dijkstra_prio_que_result, dijkstra_prio_que_time), (bellman_ford_result, bellman_ford_time)


def run_tests(tests_pairs):
    csv_handler = open('problem_shortest_path_tests.csv', 'a')
    csv_handler.write('LP, Node number, Dijkstra Result, Dijkstra Dominate Operations, Dijkstra Time, Dijkstra Priority Queue Result, Dijkstra Priority Queue Dominate Operations, Dijkstra Priority Queue Time, Bellman-Ford Result, Bellman-Forda Dominate Operations, Bellman-Ford Time \n')
    csv_handler.close()
    test_lp = 1
    for test_pair in tests_pairs:
        csv_handler = open('problem_shortest_path_tests.csv', 'a')
        file_name, amount_nodes = test_pair
        graph = load_graph(file_name, amount_nodes)
        result = run_test(graph)
        result_str = str(result)
        print("[{0}] Test: {1}".format(amount_nodes, result_str))
        result = "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}".format(test_lp, amount_nodes, result[0][0][0], result[0][0][1], result[0][1], result[1][0][0], result[1][0][1], result[1][1], result[2][0][0], result[2][0][1], result[2][1]) + "\n"
        csv_handler.write(result)
        csv_handler.close()
        test_lp += 1

result = load_graph('test_0_0_10', 10)
file_names = load_test_meta('test_meta_data')
tests_pairs = get_tuples_by_file_name(file_names)
run_tests(tests_pairs)