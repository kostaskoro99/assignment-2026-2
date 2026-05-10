# assignment-2026-2
Second assignment for the 2026 course. The assignment can be found [here](https://github.com/dmst-algorithms-course/assignment-2026-2/blob/main/rendezvous.pdf).
import sys
from collections import deque
import bisect

class GraphNavigator:
    def __init__(self, num_nodes, edges, is_directed=False):
        self.n = num_nodes
        self.adj = [[] for i in range(num_nodes)]
        self.is_directed = is_directed

for u, v in edges:
            bisect.insort(self.adj[u], v)
            if not is_directed:
                bisect.insort(self.adj[v], u)

    def find_parity_meeting(self, start_a, start_b):
        ""  Αναζήτηση σημείου συνάντησης (node, parity).
        Επιστρέφει (node, time, path_a, path_b) ή None.
        ""
   # bfs_data[node][parity] = dist 
            def get_bfs_map(start_node):
            dist_map = {}
            queue = deque([(start_node, 0, 0)]) # node, parity, distance
            dist_map[(start_node, 0)] = (0, [start_node])
while queue:
                u, p, d = queue.popleft()
                for v in self.adj[u]:
                    new_p = 1 - p
                    if (v, new_p) not in dist_map:
                        new_path = dist_map[(u, p)][1] + [v]
                        dist_map[(v, new_p)] = (d + 1, new_path)
                        queue.append((v, new_p, d + 1))
            return dist_map

        map_a = get_bfs_map(start_a)
        map_b = get_bfs_map(start_b)
        best_meeting = None
        min_time = float('inf')

        for node in range(self.n):
            for p in [0, 1]:
                if (node, p) in map_a and (node, p) in map_b:
