# main idea:

# 1. triangulation of graph
# 2. remove a non-essential node between a pair of CONVEX polygons (triangles and rectangles)
# 3. repeat until step 2 is no longer possible

# list of tuples containing the vertices?
from Map import Map
# from shapely.geometry import Polygon
# from shapely.ops import unary_union
from shapely import *


class NavMesh():

    def __init__(self, my_map):
        self.graph = my_map
        # self.abstract1 = []
        # self.abstract2 = []

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

    def merge_new(self, rect1, rect2):
        # merging two rectangles
        polygons = [rect1, rect2]
        new_poly = unary_union(polygons)
        cent = new_poly.centroid
        cent_node = (int(cent.x), int(cent.y))
        return cent_node

    def rectangles(self):
        polygonsA = []
        for x in range(0, 16):
            for y in range(0, 16):
                # THIS IS WORKING IT IS JUST LIKE ALSO NOT WORKING
                if ((x, y)) in self.graph.entrances:
                    corner1 = (x, y)
                    y2 = y
                    for i in range(16):
                        if (x, y2) in self.graph.removedNodes or x < 0 or y2 < 0:
                            # check to see in removed list or < than edge
                            y2 += 1
                            corner2 = (x, y2)
                            break
                        else:
                            corner2 = (x, 0)
                            y2 -= 1
                    x3 = x
                    for i in range(16):
                        if (x3, y) in self.graph.removedNodes or x3 < 0 or y < 0:
                            x3 += 1
                            corner3 = (x3, y)
                            break
                        else:
                            corner3 = (0, y)
                            x3 -= 1
                    y3 = y
                    for i in range(16):
                        if (x3, y3) in self.graph.removedNodes:#  or x3 < 0 or y3 < 0:
                            y3 += 1
                            corner4 = (x3, y3)
                        else:
                            corner4 = (0, 0)
                            y3 -= 1

                    polygonsA.append([corner1, corner2, corner3, corner4])
        return polygonsA

        # cluster B
        # polygonsB = []

        # cluster C

    def rectangulate3(self):
        # cluster A

        quadrant1 = []  #
        quadrant2 = []
        quadrant3 = []
        quadrant4 = []

        pass

    def obstacle_detected(self, x, y):
        while not node[x][y]:
            pass


my_map = Map()
print("map generated")
print(list(my_map.gr.neighbors((15, 35))))
test = NavMesh(my_map)

print(test.graph.entrances)
# print(list(test.graph.gr.neighbors((12, 5))))
print(test.merge((15, 35), (14, 3)))

# testing
polygon1 = Polygon([(16, 35), (18, 32), (31, 38)])
polygon2 = Polygon([(16, 35), (21, 47), (31, 38)])

print("centroid value: ", test.merge_new(polygon1, polygon2))
print("Cluster A: ", test.rectangles())

polygons = [polygon1, polygon2]

u = unary_union(polygons)
print(u)
cent = u.centroid
print(cent)
print(int(cent.x))
print(int(cent.y))
new_cent = (22, 38)

