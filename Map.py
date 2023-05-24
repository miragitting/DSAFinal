from astar import *

class Map():
    #height, width, and have a remove function that removes a vertex
    def __init__(self):

        #Hard coded definition of what a map is
        self.actual = nx.grid_graph((64,64))


        self.entrances = [(15,3),(16,3),(15,20),(16,20),(15,35),(16,35),(15,60),(16,60),
                          (31,5),(32,5),(31,22),(32,22),(31,38),(32,38),(31,63),(32,63),
                          (47,3),(48,3),(47,26),(48,26),(47,32),(48,32),(47,61),(48,61),
                          (1,15),(1,16),(17,15),(17,16),(34,15),(34,16),(56,15),(56,16),
                          (5,31),(5,32),(18,31),(18,32),(39,31),(39,32),(53,31),(53,32),
                          (7,47),(7,48),(21,47),(21,48),(36,47),(36,48),(57,47),(57,48),]

        self.removedNodes = [(3,13),(1,25),(2,4),(46,35),(53,23),(56,32),(31,23),(2,5),
                             (60,60),(12,22),(18,50),(31,40),(2,31),(45,54),(23,59),(62,52),
                             (1,43),(23,4),(25,6),(2,36),(37,52),(46,43),(23,54),(34,61),]


        self.secondLayerEntrances = []
        for i in self.entrances:
            if i[0] == 31 or i[0] == 32 or i[1] == 31 or i[1] == 32:
                self.secondLayerEntrances.append(i)

        for i in self.removedNodes:
            self.actual.remove_node(i)

        self.firstLayer = None




    #CLUSTERS
    def getCluster(self, node):

        for n in self.removedNodes:
            if(node[0] == n[0] and node[1] == n[1]):
                return "The node passed in has previously been removed"

        if(node[0] not in range(0,63) and node[1] not in range(0,63)):
            return "The node passed is not in the graph"
        #A cluster is a 16 x 16 square of nodes.
        #This function takes in a node and returns the cluster it lies on

        if node[0] in range(0,15) and node[1] in range(0,15):
            return "A"
        if node[0] in range(16,31) and node[1] in range(0,15):
            return "B"
        if node[0] in range(32,47) and node[1] in range(0,15):
            return "C"
        if node[0] in range(48,63) and node[1] in range(0,15):
            return "D"

        if node[0] in range(0,15) and node[1] in range(16,31):
            return "E"
        if node[0] in range(16,31) and node[1] in range(16,31):
            return "F"
        if node[0] in range(32,47) and node[1] in range(16,31):
            return "G"
        if node[0] in range(48,63) and node[1] in range(16,31):
            return "H"

        if node[0] in range(0,15) and node[1] in range(32,47):
            return "I"
        if node[0] in range(16,31) and node[1] in range(32,47):
            return "J"
        if node[0] in range(32,47) and node[1] in range(32,47):
            return "K"
        if node[0] in range(48,63) and node[1] in range(32,47):
            return "L"

        if node[0] in range(0,15) and node[1] in range(48,63):
            return "M"
        if node[0] in range(16,31) and node[1] in range(48,63):
            return "N"
        if node[0] in range(32,47) and node[1] in range(48,63):
            return "O"
        if node[0] in range(48,63) and node[1] in range(48,63):
            return "P"

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


    def largeNodeDeleter(self, x, y, xshift, yshift):
        relist = []
        for i in range(xshift,xshift+x+1):
            for j in range(yshift,yshift+y+1):
                #if((i,j))
                relist.append((i,j))

        #add removed nodes the self.removed nodes
        for i in relist:
            self.removedNodes.append(relist)
        return relist



    def createFirstLayer(self):
        self.firstLayer = nx.Graph()
        for i in self.entrances:
            self.firstLayer.add_node
        # want to connect the entrances of each cluster
        # get the entrance to each cluster

        entrancesA = self.getEntrances('A')
        self.firstLayer.add_edge(entrancesA[0], entrancesA[1], weight = len(astar(entrancesA[0], entrancesA[1], self.actual))-1)
        entrancesB = self.getEntrances('B')
        self.firstLayer.add_edge(entrancesB[0], entrancesB[1], weight = len(astar(entrancesB[0], entrancesB[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesB[0], entrancesB[2], weight = len(astar(entrancesB[0], entrancesB[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesB[1], entrancesB[2], weight = len(astar(entrancesB[1], entrancesB[2], self.actual))-1)
        entrancesC = self.getEntrances('C')
        self.firstLayer.add_edge(entrancesC[0], entrancesC[1], weight = len(astar(entrancesC[0], entrancesC[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesC[0], entrancesC[2], weight = len(astar(entrancesC[0], entrancesC[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesC[1], entrancesC[2], weight = len(astar(entrancesC[1], entrancesC[2], self.actual))-1)
        entrancesD = self.getEntrances('D')
        self.firstLayer.add_edge(entrancesD[0], entrancesD[1], weight = len(astar(entrancesD[0], entrancesD[1], self.actual))-1)
        entrancesE = self.getEntrances('E')
        self.firstLayer.add_edge(entrancesE[0], entrancesE[1], weight = len(astar(entrancesE[0], entrancesE[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesE[0], entrancesE[2], weight = len(astar(entrancesE[0], entrancesE[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesE[1], entrancesE[2], weight = len(astar(entrancesE[1], entrancesE[2], self.actual))-1)
        entrancesF = self.getEntrances('F')
        self.firstLayer.add_edge(entrancesF[0], entrancesF[1], weight = len(astar(entrancesF[0], entrancesF[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesF[0], entrancesF[2], weight = len(astar(entrancesF[0], entrancesF[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesF[0], entrancesF[3], weight = len(astar(entrancesF[0], entrancesF[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesF[1], entrancesF[2], weight = len(astar(entrancesF[1], entrancesF[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesF[1], entrancesF[3], weight = len(astar(entrancesF[1], entrancesF[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesF[2], entrancesF[3], weight = len(astar(entrancesF[2], entrancesF[3], self.actual))-1)
        entrancesG = self.getEntrances('G')
        self.firstLayer.add_edge(entrancesG[0], entrancesG[1], weight = len(astar(entrancesG[0], entrancesG[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesG[0], entrancesG[2], weight = len(astar(entrancesG[0], entrancesG[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesG[0], entrancesG[3], weight = len(astar(entrancesG[0], entrancesG[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesG[1], entrancesG[2], weight = len(astar(entrancesG[1], entrancesG[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesG[1], entrancesG[3], weight = len(astar(entrancesG[1], entrancesG[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesG[2], entrancesG[3], weight = len(astar(entrancesG[2], entrancesG[3], self.actual))-1)
        entrancesH = self.getEntrances('H')
        self.firstLayer.add_edge(entrancesH[0], entrancesH[1], weight = len(astar(entrancesH[0], entrancesH[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesH[0], entrancesH[2], weight = len(astar(entrancesH[0], entrancesH[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesH[1], entrancesH[2], weight = len(astar(entrancesH[1], entrancesH[2], self.actual))-1)
        entrancesI = self.getEntrances('I')
        self.firstLayer.add_edge(entrancesI[0], entrancesI[1], weight = len(astar(entrancesI[0], entrancesI[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesI[0], entrancesI[2], weight = len(astar(entrancesI[0], entrancesI[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesI[1], entrancesI[2], weight = len(astar(entrancesI[1], entrancesI[2], self.actual))-1)
        entrancesJ = self.getEntrances('J')
        self.firstLayer.add_edge(entrancesJ[0], entrancesJ[1], weight = len(astar(entrancesJ[0], entrancesJ[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesJ[0], entrancesJ[2], weight = len(astar(entrancesJ[0], entrancesJ[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesJ[0], entrancesJ[3], weight = len(astar(entrancesJ[0], entrancesJ[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesJ[1], entrancesJ[2], weight = len(astar(entrancesJ[1], entrancesJ[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesJ[1], entrancesJ[3], weight = len(astar(entrancesJ[1], entrancesJ[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesJ[2], entrancesJ[3], weight = len(astar(entrancesJ[2], entrancesJ[3], self.actual))-1)
        entrancesK = self.getEntrances('K')
        self.firstLayer.add_edge(entrancesK[0], entrancesK[1], weight = len(astar(entrancesK[0], entrancesK[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesK[0], entrancesK[2], weight = len(astar(entrancesK[0], entrancesK[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesK[0], entrancesK[3], weight = len(astar(entrancesK[0], entrancesK[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesK[1], entrancesK[2], weight = len(astar(entrancesK[1], entrancesK[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesK[1], entrancesK[3], weight = len(astar(entrancesK[1], entrancesK[3], self.actual))-1)
        self.firstLayer.add_edge(entrancesK[2], entrancesK[3], weight = len(astar(entrancesK[2], entrancesK[3], self.actual))-1)
        entrancesL = self.getEntrances('L')
        self.firstLayer.add_edge(entrancesL[0], entrancesL[1], weight = len(astar(entrancesL[0], entrancesL[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesL[0], entrancesL[2], weight = len(astar(entrancesL[0], entrancesL[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesL[1], entrancesL[2], weight = len(astar(entrancesL[1], entrancesL[2], self.actual))-1)
        entrancesM = self.getEntrances('M')
        self.firstLayer.add_edge(entrancesM[0], entrancesM[1], weight = len(astar(entrancesM[0], entrancesM[1], self.actual))-1)
        entrancesN = self.getEntrances('N')
        self.firstLayer.add_edge(entrancesN[0], entrancesN[1], weight = len(astar(entrancesN[0], entrancesN[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesN[0], entrancesN[2], weight = len(astar(entrancesN[0], entrancesN[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesN[1], entrancesN[2], weight = len(astar(entrancesN[1], entrancesN[2], self.actual))-1)
        entrancesO = self.getEntrances('O')
        self.firstLayer.add_edge(entrancesO[0], entrancesO[1], weight = len(astar(entrancesO[0], entrancesO[1], self.actual))-1)
        self.firstLayer.add_edge(entrancesO[0], entrancesO[2], weight = len(astar(entrancesO[0], entrancesO[2], self.actual))-1)
        self.firstLayer.add_edge(entrancesO[1], entrancesO[2], weight = len(astar(entrancesO[1], entrancesO[2], self.actual))-1)
        entrancesP = self.getEntrances('P')
        self.firstLayer.add_edge(entrancesP[0], entrancesP[1], weight = len(astar(entrancesP[0], entrancesP[1], self.actual))-1)

        interEdges = [(entrancesA[0], entrancesB[0]), (entrancesA[1], entrancesE[1]), (entrancesB[1], entrancesC[0]), (entrancesB[2], entrancesF[2]),
                      (entrancesC[1], entrancesD[0]), (entrancesC[2], entrancesG[3]), (entrancesD[1], entrancesH[1]), (entrancesE[0], entrancesF[0]),
                      (entrancesE[2], entrancesI[1]), (entrancesF[1], entrancesG[0]), (entrancesF[3], entrancesJ[2]), (entrancesG[1], entrancesH[0]),
                      (entrancesG[3], entrancesK[2]), (entrancesH[2], entrancesL[1]), (entrancesI[0], entrancesJ[0]), (entrancesI[2], entrancesM[1]),
                      (entrancesJ[1], entrancesK[0]), (entrancesJ[3], entrancesN[2]), (entrancesK[3], entrancesO[2]), (entrancesL[2], entrancesP[1]),
                      (entrancesM[0], entrancesN[0]), (entrancesN[1], entrancesO[0]), (entrancesO[1], entrancesP[0]),]

        for i in interEdges:
            self.firstLayer.add_edge(i[0], i[1], weight = 1)


    def findPath(self, start, goal):
        # get the cluster of start
        start_cluster = self.getCluster(start)
        goal_cluster = self.getCluster(goal)

        if goal_cluster == start_cluster:
            return astar(start, goal, self.actual)

        startEntrances = self.getEntrances(start_cluster)
        startPaths = []
        for entrance in startEntrances:
            startPaths.append(astar(start, entrance, self.actual))
            self.firstLayer.add_edge(start, entrance, weight = len(startPaths[-1])-1)


        # repeat with goal
        goalEntrances = self.getEntrances(goal_cluster)
        goalPaths = []
        for entrance in goalEntrances:
            goalPaths.append(astar(goal, entrance, self.actual))
            self.firstLayer.add_edge(goal, entrance, weight = len(goalPaths[-1])-1)

        #perform a star from start to goal on first layer of abstraction
        abstractMoves = astar(start, goal, self.firstLayer)
        print("abstract moves: ", abstractMoves)
        for i in startPaths:
            if i[-1] == abstractMoves[1]:
                return i

        # take first step and find corresponding path in the cache

        #remove the start and goal nodes from the abstract map
