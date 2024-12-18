#prototype pathfinding algorithm. This one is recursive, and would be very expensive to run on larger graphs

from graph import graph

def recursive_search(graph, start, end, seen_nodes):
    # if we have already looked at this node then don't look again
    if start in seen_nodes:
        return False
    seen_nodes.append(start)

    # Get this node as a starting point
    this_node = graph[start]

    # Get its list of edges
    edge_list = this_node.get_edge_list()

    # If this end is directly connected then concatenate the end node with this node, get the weight
    # and return them as an array.  i.e. [ 'GHJLN', 28 ]
    if end in edge_list.keys():
        edge = edge_list[end]
        weight = edge.get_weight()
        found_path = [ start+end, weight ]
        return found_path
    else:

        # If this node is not attached to the end node, then look again from this nodes edges
        edges = this_node.get_edge_list()

        results = []
        for this_end in edges.keys():

            print(f'Recursively searching from {this_end} to {end}')
            # Make sure we take a copy of the seen_nodes so that we explore each path independently
            result = recursive_search(graph, this_end, end, seen_nodes.copy())

            # If we get a result, then concatenate this edge to the path and accumulate the additional weight
            if result:
                print(f'Checking from {this_end} to {end} have weight {result[1]}')
                edge = edges[this_end]
                path = result[0]
                weight = result[1]
                path = start+path
                weight = weight + edge.get_weight()
                found_path = [ path, weight ]
                results.append(found_path)

        # if we have no result
        if len(results) == 0:
            return False
        else:
            shortest_path = results.pop(0)
            for result in results:
                if result[1] < shortest_path[1]:
                    shortest_path = result

            return shortest_path


graph = graph("test_graph.txt")

start = 'M'
end = 'N'

seen_nodes = []
result = recursive_search(graph.get_graph(), start, end, seen_nodes)
path = result[0]
weight = result[1]
print(f'Found path { path } with weight {weight}')