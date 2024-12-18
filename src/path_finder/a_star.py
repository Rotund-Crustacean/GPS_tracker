from src.path_finder.graph import graph
from src.path_finder.a_star_active_list_node import active_list_node

#Non-functional

class a_star:
    def __init__(self,graph):
        self.graph = graph
        self.active_list = []

        #getters
        def get_graph(self):
            return self.graph

        def get_active_list(self):
            return self.active_list

        def set_active_list(self, new_active_list):
            self.active_list = new_active_list


        #finds difference between two values
    @staticmethod
    def __find_diff(num1, num2):
        num1 = float(num1)
        num2 = float(num2)
        if num1 > num2:
            return num1 - num2
        else:
            return num2 - num1

    #calculates manhattan heuristic
    def __calc_dist_heuristic(self,node1,node2):
        lat_diff = a_star.__find_diff(node1.get_lat(), node2.get_lat())
        lon_diff = a_star.__find_diff(node1.get_lon(), node2.get_lon())
        dist = lat_diff + lon_diff
        return dist

    #finds closest node to given coordinates.
    def __find_closest_node(self, lon, lat):
        smallest_dist = 9999999999999999999999999
        for node in self.graph.get_graph():
            #can't use __calc_dist_heuristic - no second node
            #finding distance from coord to node for each node
            lat_diff = a_star.__find_diff(lat, node.get_lat())
            lon_diff = a_star.__find_diff(lon, node.get_lon())
            #manhattan heuristic
            dist = lon_diff + lat_diff

            #finding smallest dist value
            if dist < smallest_dist:
                smallest_dist = dist
                closest_node = node

        return closest_node

        #calculates total weight value for a node by calculating heuristic, then finding the route_weight of
        #the previous active list node, then the edge weight to the current route
        def __calc_total_node_value(self, current_node, prev_active_list_node, end_node):
            #calculating heuristic weight
            dist = a_star.__calc_dist_heuristic(current_node, end_node)
            #finding route_weight of previous node
            route_weight = prev_active_list_node.get_route_weight()
            #finding edge_weight
            prev_node = prev_active_list_node.get_node()

            #iterating through prev_node.edge_list to find edge to current node
            for i in prev_node.get_edge_list():
                if i.get.end() == current_node.get_node_id():
                    edge_weight = i.get_weight()
            total = float(dist) + float(route_weight) + float(edge_weight)
            return(total)

        #evaluates if node should be added to list and values it should have, then adds it
        def __evaluate_node(self, node, prev_active_list_node, end_node):
            route_weight = __calc_total_node_value(self, active_list_node, end_node)
            #checking node id for repeated nodes. should create a new active node with this node
            #if this route is better or this node isn't already in the list
            active_list = self.get_active_list()
            #check boolean to prevent two identical active nodes from being appended to the list
            repeat = False
            for i in self.get_active_list():
                temp_node = i.get_node()
                #if this node is already in the active_nodes_list
                if temp_node.get_node_id() == node.get_node_id():
                    repeat = True
                    #if this path is less weight than
                    if i.get_route_weight() > route_weight:
                        #replacing worse route
                        active_list.remove(i)
                        new_active_node = active_list_node(node,prev_active_list_node,route_weight)
                        active_list.append(new_active_node)
            #if the node isn't already in the list
            if not repeat:
                new_active_node = active_list_node(node, prev_active_list_node, route_weight)
                active_list.append(new_active_node)


    def find_path(self,start_lon, start_lat, end_lon, end_lat):
        #setting up initial conditions for the algorithm to run
        start_node = a_star.__find_closest_node(start_lon, start_lat)
        end_node = a_star.__find_closest_node(end_lon, end_lat)
        start_active_node = active_list_node(start_node, 'NULL', 0)
        current_node = start_node

        #while current_node != end_node:





