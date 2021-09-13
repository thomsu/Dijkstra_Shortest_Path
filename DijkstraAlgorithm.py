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

    def shortest_distance(self, start, end=None):
        return self.dijkstra(start, end)[0]
    
    def shortest_path(self, start, end):
        if end not in self.adjacency_list: return 'Invalid Ending Node'
        prev_node = self.dijkstra(start, end)[1]
        if not prev_node: return 'Invalid Starting Node'
        path, node = [end], end
        
        while prev_node[node] != None:
            path.append(prev_node[node])
            node = prev_node[node]
            
        return ' -> '.join(path[::-1])    
    
    def dijkstra(self, start, end=None):
        if start not in self.adjacency_list: return 'Invalid Starting Node', {}
        h = [(0, start, None)]
        heapq.heapify(h)
        distance = {k : float('inf') for k in self.adjacency_list}
        prev_node = {}
        
        while h:
            d, v, w = heapq.heappop(h)
            if v == end: 
                prev_node[v] = w
                return d, prev_node
            if d >= distance[v]: continue
            distance[v] = d
            prev_node[v] = w
            for u, l in self.adjacency_list[v]:
                heapq.heappush(h, (d+l, u, v))
        
        return distance, prev_node
