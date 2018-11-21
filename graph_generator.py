import random
import time

def is_diagonal(col, row):
    return col == row

def generate_graph(amount_node, no_exist_edge_value):
    #initialize matrix n x n
    graph = [ [ None ] * amount_node ] * amount_node 

    for i in range(amount_node):
        graph[i] = random.sample(range(1, 100), amount_node)
    
    for i in range(amount_node):
        for j in range(amount_node):
            if is_diagonal(i, j):
                graph[i][j] = no_exist_edge_value

    return graph