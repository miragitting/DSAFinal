# DSAFinal

    Map.py - Contains class Map and logic for the 64 64 graph of nodes. Also has cluster implementation
        Methods:
            getCluster - returns the Cluster that contains the specific node inputed
            getEntrances - returns entrances associated with the Cluster inputed
            nodeRemover - removes a node
            largeNodeDeleter - deletes large chunks of nodes
            createFirstLayer - creates first level abstraction of the map (just entrance nodes) 
            findPath - uses Astar to path find
  
    abstraction.py - Contains logic for original Nav mesh implementation plan. 
        Methods used: 
        merge_new - uses Shapely to merge two rectangles that share an edge and returns the centroid of the new rectangle.
        rectangles - split cluster into rectangular polygons based on entrance and obstacle location. Started hard coding this for cluster A
        All other methods were experimental and prior versions of what was achieved
        Also includes  code at the bottom of the file to test methods
          
    astar.py - function for pathfinding algorithm. 
        Utilizes most of the logic from Snake but sets the start node at index 0 of the priority queue.
        All other nodes are added to the graph after that in order. 
        Becuase obstacles are removed nodes, we did not implement logic in this to remove obstacle nodes from the graph
