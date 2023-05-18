import networkx as nx
class Map():
    #height, width, and have a remove function that removes a vertex
    def __init__(self, height, width):
        
        self.gr = nx.grid_graph((height, width))
        
    def removeNode(self, x, y):
        self.gr.remove_node((x,y))
        
    def neighbors(self, x, y):
        return self.gr.neighbors((x,y))

