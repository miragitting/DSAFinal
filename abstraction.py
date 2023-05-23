# main idea:

# 1. triangulation of graph
# 2. remove a non-essential node between a pair of CONVEX polygons (triangles and rectangles)
# 3. repeat until step 2 is no longer possible

# list of tuples containing the vertices?
from Map import Map
#from shapely.geometry import Polygon
#from shapely.ops import unary_union
from shapely import *

class NavMesh():

    def __init__(self, my_map):
        self.graph = my_map
        #self.abstract1 = []
        #self.abstract2 = []

    def triangulate(self):
        for node in self.graph.entrances:

            pass

    def merge(self, a, b):
        # merge the graph into one polygon:
        # find a pair of adjacent nodes (two nodes that share an edge between them)
        # NEED TO MAKE THIS CHECK
        # ESPECIALLY ON ENTRANCES

        c = []
        for node in self.graph.entrances:
            if node == a:
                a_n = self.graph.gr.neighbors(a)
                if b in a_n:
                    for v in a_n:
                        c.append(v)
                    # c.get -1 index
                    # find in b list
                else:
                    # return merge on different pair of nodes
                    pass
        return c
        # whose surfaces face the same direction (don't have to worry about this - 2D surface)

        # check to see if both nodes share the same two points along their shared edge.
        # if the two endpoints of those edges aren't the same, we can't merge these nodes

        # attempt to eliminate the edge and merge the remaining vertices into a single convex polygon
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

    def rectangles(self):
        pass

    def merge_new(self, rect1, rect2):
        polygons = [rect1, rect2]
        new_poly = unary_union(polygons)
        cent = new_poly.centroid
        x = int(cent.x)
        y = int(cent.y)
        cent_node = (x, y)
        return cent_node


my_map = Map()
print("map generated")
print(list(my_map.gr.neighbors((15, 35))))
test = NavMesh(my_map)

print(test.graph.entrances)
#print(list(test.graph.gr.neighbors((12, 5))))
print(test.merge((15, 35), (14, 3)))

#test
polygon1 = Polygon([(16, 35), (18, 32), (31, 38)])
polygon2 = Polygon([(16, 35), (21, 47), (31, 38)])

polygons = [polygon1, polygon2]

u = unary_union(polygons)
print(u)
cent = u.centroid
print(cent)
print(int(cent.x))
print(int(cent.y))
new_cent = (22, 38)

print(test.merge_new(polygon1, polygon2))
