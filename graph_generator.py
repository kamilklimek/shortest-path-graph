import random
import time
import copy

def is_diagonal(col, row):
    return col == row

def generate_graph(amount_node, no_exist_edge_value):
    #initialize matrix n x n
    graph = [ [ None ] * amount_node ] * amount_node 

    for i in range(amount_node):
        line = []
        for j in range(amount_node):
            line.append(random.randrange(0, 100))
        graph[i] = line
    return graph