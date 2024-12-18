#This class is intended to act as the nodes on a graph for the A* algorithm to route through
#This is currently a data class

class node:
    def __init__(self,node_id, lon, lat):
        self.node_id = node_id
        self.lon = lon
        self.lat = lat
        self.edge_list = {}

    def get_node_id(self):
        return self.node_id
    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def get_edge_list(self):
        return self.edge_list

    def add_edge(self,edge):
        self.edge_list[edge.get_end()] = edge
