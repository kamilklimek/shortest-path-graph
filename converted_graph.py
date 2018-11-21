def convert_graph_from_value_to_value(graph, old_value, new_value):
    for row_index in range(len(graph)):
        for col_index in range(len(graph[row_index])):
            if graph[row_index][col_index] == old_value:
                graph[row_index][col_index] = new_value
    
    return graph