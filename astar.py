import math
import networkx as nx
import numpy as np
import heapq
from Map import Map

class PriorityQueue():

    def __init__(self):
        self.items = []
        self.true_pri = {}

    def put(self, pri, item):
        # put the item in the heap with the new priority
        heapq.heappush(self.items, (pri, item))

        # update our "correct" priority values
        if item in self.true_pri:
            old_pri = self.true_pri[item]
            self.true_pri[item] = min(old_pri, pri)
        else:
            self.true_pri[item] = pri


    def pop(self):
        if len(self.items) == 0:
            return None,None
        pri, item = heapq.heappop(self.items)

        while pri != self.true_pri[item]:
            if len(self.items) == 0:
                return None,None
            pri, item = heapq.heappop(self.items)

        return pri, item

    def __len__(self):
        return len(self.items)


INF = 99999999999999999
def astar_AI(bstate, start, goal):

    #source = np.array(np.where(bstate == -2))
    #target = np.array(np.where(bstate == 1))
    source = start
    target = goal

    #obstacles = np.array(np.where(bstate < 0))

    #x_source = source[0][0]
    #y_source = source[1][0]

    #x_target = target[0][0]
    #y_target = target[1][0]

    #start = (x_source, y_source)
    #end = (x_target, y_target)

    gr = Map()

    preds = {start: None}
    dist = {start: 0}
    queue = PriorityQueue()

    for i in range(bstate.shape[0]):
        for j in range(bstate.shape[1]):
            if bstate[i, j] == -1:
                gr.remove_node((i, j))
                # nothing happens w pq
            elif bstate[i, j] == -2:
                queue.put(0, (i, j))

            else:
                queue.put(INF, (i,j))
                dist[(i, j)] = INF

    current_node = None

    while len(queue) > 0 and current_node != end: # end not in preds
        dist_to_current, current_node = queue.pop()

        neighbors = gr.neighbors(current_node)

        for n in neighbors:
            # dist from source to current, dist from current to n, heuristic
            new_dist = dist[current_node] + 1 # edge weight between neighbor and current node
            new_pri = new_dist + math.dist(n, end)

            if new_dist < dist[n]:
                dist[n] = new_dist
                preds[n] = current_node
                queue.put(new_pri, n)
    steps = [end]
    while steps[0] != start:
        # insert pred of what is at index[0] at [0]
        pass
    return steps # or first move index [] in array
    #print(queue)
    #  chain of preds ?
    # subtract x's and y's from eachother