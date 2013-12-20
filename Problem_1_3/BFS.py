# Script to implement BFS to find a path from source to destination

#!/usr/bin/env python 

# Method to find a path using BFS
def bfs(G, F, source, sink, nim):
    queue = [source]                 
    paths = {source: []}
    all_paths = []
    while queue:
        u = queue.pop(0)
	for v in (G[u]):
		if len(v) != 0:
			diff = G[u][v]['max'] - F[nim[u]][nim[v]]
			
			# Add an adjacent node to path only if its not already present and residual flow > 0
			if diff > 0 and v not in paths:
				paths[v] = paths[u] + [(u,v)]
				if v == sink:
					all_paths = paths[v]
				    	return all_paths
				queue.append(v)
    return None
