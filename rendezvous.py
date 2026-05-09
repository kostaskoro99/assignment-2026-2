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
