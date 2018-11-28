import math
nodes_number = [10, 20, 40, 80, 160, 320, 640, 1280, 2560, 5120]

bellman =[]
dijstra = []
dijstra_prio = []

for node in nodes_number:
    bell = node * node * node
    dij = node * node
    dij_prio = math.exp(1)  * math.log(node)
    
    print("[{0}] {1} === {2} === {3}".format(node, bell, dij, dij_prio))

