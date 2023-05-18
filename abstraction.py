# main idea:

# 1. triangulation of graph
# 2. remove a non-essential node between a pair of CONVEX polygons (triangles and rectangles)
# 3. repeat until step 2 is no longer possible

# list of tuples containing the vertices?

class NavMesh():

    def __init__(self, graph):
        # self.graph from map class
        pass

    def triangulate(self):

        pass

    def merge(self, a, b):
        # merge the graph into one polygon:
        # find a pair of adjacent nodes (two nodes that share an edge between them)
        # make this check
        c = []
        for node in self.graph:
            if node[0] == a[0]:
                if b[0] in a[1]:
                    for v in a[1]:
                        c.append(v)
                    # c.get -1 index
                    # find in b list
                else:
                    # return merge on different pair of nodes
                    pass

        # whose surfaces face the same direction (don't think we have to worry as much about this)

        # check to see if both nodes share the same two points along their shared edge.
        # if the two endpoints of those edges aren't the same, we can't merge these nodes

        # attempt to eliminate the edge and mege the remaining vertices into a single convex polygon
        # if you can't make a convex polygon, the nodes can't be merged.
        # if possible, delete both of the existing nodes and replace them with the new node
        # polygon C -> look at clockwise most shared vertex of A and B
        # add all of A's vertices to C's vertex list
        # L = last vertex added to A should be shared between A and B.
        # locate vertex L in B's list and add all of B's vertices to C starting with L
        # simplify the remaining polygon by eliminating any unnecessary vertices.
        # vertex is unnecessary is it is redundant (vertex is identical to the vertex immediately
        # before or after it in C's vertex list) or if it is unnecessary to maintain the shape of the
        # polygon (if we look at the edge between prev vertex and next vertex and the current vertex
        # lies somewhere on that line)

        pass