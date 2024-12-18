#This data class is an adaptation of the graph_node class, but extended to contain information relevant to pathfinding
class active_list_node:
    def __init__(self, node, prev_active_list_node, route_weight):
        self.node = node
        self.prev_active_list_node = prev_active_list_node
        self.route_weight = route_weight
        self.complete = False

        #getters

        def get_node(self):
            return self.node

        def get_prev_active_list_node(self):
            return self.prev_active_list_node

        def get_route_weight(self):
            return self.route_weight

        def get_complete(self):
            return self.complete

        #setters

        def set_prev_active_list_node(self, prev_node):
            self.prev_active_list_node = prev_node

        def set_route_weight(self, weight):
            self.route_weight = weight

        def set_complete(self):
            self.complete = True
