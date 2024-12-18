#generic test area

#testing pathfinding algorithm

#for i in temp_graph.get_graph():
#    print(f'Node: {i.get_node_id()} with lon {i.get_lon()} and lat {i.get_lat()}.')
#    for j in i.get_edge_list():
#        print(f'Edge with end node {j.get_end()} and weight {j.get_weight()}.')

from src.path_finder.graph import graph
# from src.path_finder.a_star import a_star

#defining inputs for testing purposes
file_name = '/Users/ewan/sandbox/gps_tracker/src/path_finder/test_graph.txt'
graph = graph(file_name).get_graph()

for i in graph:
    print(f'Node: {i}')
    node = graph[i]
    for j in node.get_edge_list():
        print(f' Edge: {j}')
