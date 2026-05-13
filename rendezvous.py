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
                    time_a, path_a = map_a[(node, p)]
                    time_b, path_b = map_b[(node, p)]
                    if time_a == time_b:
                        if time_a < min_time:
                            min_time = time_a
                            best_meeting = (node, time_a, path_a, path_b)
        return best_meeting

    def is_bipartite(self):
        """Ελέγχει αν ο γράφος είναι διμερής και επιστρέφει τα σύνολα (color map)."""
        color = {}
        for i in range(self.n):
            if i not in color:
                queue = deque([i])
                color[i] = 0
                while queue:
                    u = queue.popleft()
                    for v in self.adj[u]:
                        if v not in color:
                            color[v] = 1 - color[u]
                            queue.append(v)
                        elif color[v] == color[u]:
                            return False, None
                            return True, color

def print_history(path_a, path_b, node, time):
    for t in range(len(path_a)):    
     print(f"{t}: Alice at {path_a[t]}, Bob at {path_b[t]}")
     print(f"Meeting at node {node} at time step {time}")
  
def main():
    print("--- Program Started ---") 
     # Διαχείριση παραμέτρων: [-d] filename
    args = sys.argv[1:]
    is_directed = False 
    if "-d" in args:
        is_directed = True
        args.remove("-d") 

    if not args:
        print("Usage: python rendezvous.py <graph_file.txt>")
        return
    
    filename = args[0]   
    print(f"--- Looking for file: {filename} ---") 
 
    try:
        with open(filename, 'r') as f:
            lines = [line.split() for line in f if line.strip()]
        
        if not lines: 
            print("The file is empty!")
            return
        
        print(f"--- File loaded. Found {len(lines)} lines ---") 
        
        # 1η γραμμή: Κόμβοι και Ακμές
        num_nodes, num_edges = map(int, lines[0])
        
        # Τελευταία γραμμή: Alice και Bob
        start_a, start_b = map(int, lines[-1])
        
        # Ενδιάμεσες γραμμές: Ακμές
        edges = [map(int, lines[i]) for i in range(1, num_edges + 1)]
        
        gn = GraphNavigator(num_nodes, edges, is_directed)
        
        result = gn.find_parity_meeting(start_a, start_b)

        if result:
            node, time, path_a, path_b = result
            print_history(path_a, path_b, node, time)
            
        else:
            print("No meeting is possible")
            
        if not is_directed: # Λογική για μη κατευθυνόμενους (προσθήκη ακμής)
            bipartite, colors = gn.is_bipartite()
            
            # Αν ο γράφος είναι διμερής και είναι σε διαφορετικά σύνολα, προσθέτουμε ακμή
            if bipartite and colors[start_a] != colors[start_b]:
                print("Adding 1 edge")
