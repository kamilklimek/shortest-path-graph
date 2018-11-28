from graph_generator import generate_graph
import os

directory_path = 'tests/'
file_handler_meta_test_data = open('test_meta_data', 'a')
amount_nodes = 10
for i in range(10):
    for j in range(10):
        graph = generate_graph(amount_nodes, 0)
        test_name = "test_" + str(i) + "_" + str(j) + "_" + str(amount_nodes)
        file_handler_meta_test_data.write(test_name + ":" + str(amount_nodes) + "\n")
        file_name = os.path.join(directory_path, test_name)
        file_handler = open(file_name, "w")
        for x in range(len(graph)):
            for y in range(amount_nodes):
                file_handler.write(str(graph[x][y]) + " ")
            file_handler.write("\n");
        file_handler.close()
    amount_nodes = int (amount_nodes * 2)

file_handler_meta_test_data.close()