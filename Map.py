import networkx as nx
class Map():
    #height, width, and have a remove function that removes a vertex
    def __init__(self, height, width):
        
        self.gr = nx.grid_graph((height, width))
        
    def removeNode(self):
        self.gr.remove_node()
        
#    map = Map(1,5)

