# Script to find the shortest path from source to destination

#!/usr/bin/env python 

def bfs(G, F, source, sink, nim):
    queue = [source]                 
    paths = {source: []}
    all_paths = []
    while queue:
        u = queue.pop(0)	        
	for v in (G[u]):
		if len(v) != 0:
		    	if float(G[u][v]['max']) - F[nim[u]][nim[v]] > 0 and v not in paths:
		        	paths[v] = paths[u] + [(u,v)]
		        	if v == sink:
					all_paths = paths[v]
				    	return all_paths
		        	queue.append(v)
    return None
