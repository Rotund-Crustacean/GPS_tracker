#This is the implementation of graph logic using the existing node and edge classes

from src.path_finder.graph_node import node
from src.path_finder.graph_edge import edge

class graph:
    #this function is quite fradgile, needs properly formatted input file
    #node_id,lon,lat
    #-end_node-weight
    def __init__(self, file_name):
        file_name = str(file_name)
        file = open(file_name, 'r')
        lines = file.readlines()
        self.graph = {}
        for line in lines:
            #filtering for new nodes
            if line[0] != '-':
                #line formatting
                line = line.rstrip()
                line_parts = line.split(',')
                #new node object
                temp_node = node(line_parts[0],line_parts[1],line_parts[2])
                #setting new node to current node for edge additions
                current_node = temp_node
                #adding to graph list
                self.graph[temp_node.get_node_id()] = temp_node
            else:
                #line formatting
                line_parts = line.split('-')
                #new edge object
                temp_edge = edge(line_parts[1],line_parts[2])
                #adding to edge list of current node
                current_node.add_edge(temp_edge)


    def get_graph(self):
        return self.graph

