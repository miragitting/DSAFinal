import networkx as nx

class Map():
    #height, width, and have a remove function that removes a vertex
    def __init__(self):

        #Hard coded definition of what a map is
        self.gr = nx.grid_graph((64,64))


        self.entrances = [(15,3),(16,3),(15,20),(16,20),(15,35),(16,35),(15,60),(16,60),
                          (31,5),(32,5),(31,22),(32,22),(31,38),(32,38),(31,63),(32,63),
                          (47,3),(48,3),(47,26),(48,26),(47,32),(48,32),(47,61),(48,61),
                           (1,15),(1,16),(17,15),(17,16),(34,15),(34,16),(56,15),(56,16),
                          (5,31),(5,32),(18,31),(18,32),(39,31),(39,32),(53,31),(53,32),
                          (7,47),(7,48),(21,47),(21,48),(36,47),(36,48),(57,47),(57,48),]

        self.removedNodes = [(3,13),(1,25),(2,4),(46,35),(53,23),(56,32),(31,23),(2,5),
                          (60,60),(12,22),(18,50),(31,40),(2,31),(45,54),(23,59),(62,52),
                          (1,43),(23,4),(25,6),(2,36),(37,52),(46,43),(23,54),(34,61),]


    #CLUSTERS
    def clusterFinder(self, node):

        #A cluster is a 16 x 16 square of nodes.
        #This function takes in a node and returns the cluster it lies on

        #First, lets check to see if the node has been removed or is even in the graph

        for n in self.removedNodes:
            if(node[0] == n[0] and node[1] == n[1]):
                return "The node passed in has previously been removed"

        if(node[0] not in range(0,63) and node[1] not in range(0,63)):
            return "The node passed is not in the graph"

        #Tanner, feel free to change the returns if it does not line up with your pathfinding code.
        #I am just returning strings for testing reasons

        if node[0] in range(0,15) and node[1] in range(0,15):
            return "Cluster A"
        if node[0] in range(16,31) and node[1] in range(0,15):
            return "Cluster B"
        if node[0] in range(32,47) and node[1] in range(0,15):
            return "Cluster C"
        if node[0] in range(48,63) and node[1] in range(0,15):
            return "Cluster D"

        if node[0] in range(0,15) and node[1] in range(16,31):
            return "Cluster E"
        if node[0] in range(16,31) and node[1] in range(16,31):
            return "Cluster F"
        if node[0] in range(32,47) and node[1] in range(16,31):
            return "Cluster G"
        if node[0] in range(48,63) and node[1] in range(16,31):
            return "Cluster H"

        if node[0] in range(0,15) and node[1] in range(32,47):
            return "Cluster I"
        if node[0] in range(16,31) and node[1] in range(32,47):
            return "Cluster J"
        if node[0] in range(32,47) and node[1] in range(32,47):
            return "Cluster K"
        if node[0] in range(48,63) and node[1] in range(32,47):
            return "Cluster L"

        if node[0] in range(0,15) and node[1] in range(48,63):
            return "Cluster M"
        if node[0] in range(16,31) and node[1] in range(48,63):
            return "Cluster N"
        if node[0] in range(32,47) and node[1] in range(48,63):
            return "Cluster O"
        if node[0] in range(48,63) and node[1] in range(48,63):
            return "Cluster P"

    def getEntrances(self, cluster):
        elist = []

        if cluster == 'A':
            for i in self.entrances:
                if i[0] <= 15 and i[1] <=  15:
                    elist.append(i)

        if cluster == 'B':
            for i in self.entrances:
                if i[0] >= 16 and i[0] <= 31 and i[1] <=  15:
                    elist.append(i)

        if cluster == 'C':
            for i in self.entrances:
                if i[0] >= 32 and i[0] <= 47 and i[1] <=  15:
                    elist.append(i)

        if cluster == 'D':
            for i in self.entrances:
                if i[0] >= 48 and i[0] <= 63 and i[1] <=  15:
                    elist.append(i)



        if cluster == 'E':
            for i in self.entrances:
                if i[0] <= 15 and i[1] >=  16 and i[1] <= 31:
                    elist.append(i)

        if cluster == 'F':
            for i in self.entrances:
                if i[0] >= 16 and i[0] <= 31 and i[1] >=  16 and i[1] <= 31:
                    elist.append(i)

        if cluster == 'G':
            for i in self.entrances:
                if i[0] >= 32 and i[0] <= 47 and i[1] >=  16 and i[1] <= 31:
                    elist.append(i)

        if cluster == 'H':
            for i in self.entrances:
                if i[0] >= 48 and i[0] <= 63 and i[1] >=  16 and i[1] <= 31:
                    elist.append(i)



        if cluster == 'I':
            for i in self.entrances:
                if i[0] <= 15 and i[1] >= 32 and i[1] <= 47:
                    elist.append(i)

        if cluster == 'J':
            for i in self.entrances:
                if i[0] >= 16 and i[0] <= 31 and i[1] >=  32 and i[1] <= 47:
                    elist.append(i)

        if cluster == 'K':
            for i in self.entrances:
                if i[0] >= 32 and i[0] <= 47 and i[1] >=  32 and i[1] <= 47:
                    elist.append(i)

        if cluster == 'L':
            for i in self.entrances:
                if i[0] >= 48 and i[0] <= 63 and i[1] >=  32 and i[1] <= 47:
                    elist.append(i)



        if cluster == 'M':
            for i in self.entrances:
                if i[0] <= 15 and i[1] >= 48 and i[1] <= 63:
                    elist.append(i)

        if cluster == 'N':
            for i in self.entrances:
                if i[0] >= 16 and i[0] <= 31 and i[1] >=  48 and i[1] <= 63:
                    elist.append(i)

        if cluster == 'O':
            for i in self.entrances:
                if i[0] >= 32 and i[0] <= 47 and i[1] >=  48 and i[1] <= 63:
                    elist.append(i)

        if cluster == 'P':
            for i in self.entrances:
                if i[0] >= 48 and i[0] <= 63 and i[1] >=  48 and i[1] <= 63:
                    elist.append(i)



        return elist


    # Tool method that only needs to be used once, removes all of the nodes in removed nodes list
    def nodeRemover(self, nlist):
        for i in nlist:
            self.gr.remove_node((i))

#Testing stuff
map = Map()
print(map.gr)
print(len(map.removedNodes))
map.nodeRemover(map.removedNodes)
print(map.gr)
# more testing
print(map.clusterFinder((50,24)))

print(map.getEntrances('O'))

#nx.draw_networkx(map.gr)
