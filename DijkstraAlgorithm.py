import collections
import heapq

class Network:

    def __init__(self):
        self.adjacency_list = collections.defaultdict(list)

    def add_connections(self, edges, weights=[]):
        if weights == []:
            weights = [1] * len(edges)
        for (a, b), w in zip(edges, weights):
            self.adjacency_list[a].append((b, w))
            self.adjacency_list[b].append((a, w))

    def dijkstra_distance(self, start, end=None):
        if start not in self.adjacency_list: return 'Invalid Starting Node'
        h = [(0, start)]
        heapq.heapify(h)
        distance = {k : float('inf') for k in self.adjacency_list}

        while h:
            d, v = heapq.heappop(h)
            if v == end: return d
            if d >= distance[v]: continue
            distance[v] = d
            for u, l in self.adjacency_list[v]:
                heapq.heappush(h, (d+l, u))

        return distance
