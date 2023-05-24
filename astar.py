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
            return None, None
        pri, item = heapq.heappop(self.items)

        while pri != self.true_pri[item]:
            if len(self.items) == 0:
                return None, None
            pri, item = heapq.heappop(self.items)

        return pri, item

    def __len__(self):
        return len(self.items)


INF = 99999999999999999


def astar_AI(start, goal, our_graph):

    source = start
    end = goal

    gr = our_graph

    preds = {start: None}
    dist = {start: 0}
    queue = PriorityQueue()

    current_node = None

    while len(queue) > 0 and end not in preds:  # end not in preds
        dist_to_current, current_node = queue.pop()

        neighbors = gr.neighbors(current_node)

        for n in neighbors:
            # dist from source to current, dist from current to n, heuristic
            new_dist = dist[current_node] + 1  # TODO: instead of 1, edge weight between neighbor and current node
            new_pri = new_dist + math.dist(n, end)

            if new_dist < dist[n]:
                dist[n] = new_dist
                preds[n] = current_node
                queue.put(new_pri, n)
    steps = [end]
    while steps[0] is not source:
        steps.insert(0, preds[steps[0]]) # not sure if this is correct
    return steps  # or first move index [] in array
