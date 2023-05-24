# DSAFinal

Map.py - Map logic for the 64 64 graph of nodes. Also has cluster implementation

    
    abstraction.py - Contains logic for original Nav mesh implementation plan. 
    
        Methods used in testing: 
        
            merge_new: uses Shapely to merge two rectangles that share an edge and returns the centroid of the new rectangle.
        
          

astar.py - pathfinding algorithm. untilizes most of the logic from Snake but sets the start node at index 0 of the priority queue. all other nodes are added to the graph after that in order. Becuase obstacles are removed nodes, we do not have to implement logic to remove nodes from the graph



