#This class is intended to act as the edges between nodes on the graph for the A* algorithm to route through
#start and end should be node classes, with weight as the difficulty to travel between nodes.
# This is currently a data class
class edge:
    def __init__(self, end, weight):
        self.end = end
        self.weight = float(weight)

    def get_end(self):
        return self.end

    def get_weight(self):
        return self.weight
