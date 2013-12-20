#!/usr/bin/env python 

import process_input as ip
import BFS
import Modifygraph_EK as mg
import datetime as dt

file_result = open('Result_File_6_2.txt', 'ab')

def edmond_karp(G,origraph):

	#Flow matrix n * n to keep track of flow 
	n = len(G.keys()) #number of nodes
	F = [[0] * n for i in xrange(n)] #Flow, reverse edges
	
	#create key-value pairs for nodes and Flow matrix idx
	idx = {} 
	for i, node in enumerate(G.keys()):	
		idx[node] = int(i)

	max_flow = 0
	RG = G

	# Find paths from 'SS' to 'TT' to satisfy minimum number of assignments
	while True:
		path = BFS.bfs(G, F, 'SS', 'TT', idx)
		#print 'path: %s' % path
		if not path: 
			break
		#compute flow allowable for the current path
		path_flow = min(int(G[u][v]['max']) - F[idx[u]][idx[v]] for u,v in path) #Total Capacity - used capacity
		
		#modify the flow matrix with current path's flow
		for u,v in path:
			F[idx[u]][idx[v]] += path_flow
			F[idx[v]][idx[u]] -= path_flow
		
			#Create a new residual graph for 6.3
			RG[u][v]['max'] = int(RG[u][v]['max']) - path_flow

		max_flow += path_flow
	
	# Find paths from 'S' to 'T' to get maximum possible assignments
	while True:
		path = BFS.bfs(G, F, 'S', 'T', idx)
		#print 'path from ss to t: %s' % path
		if not path: 
			break
		#compute flow allowable for the current path
		path_flow = min(int(G[u][v]['max']) - F[idx[u]][idx[v]] for u,v in path) #Total Capacity - used capacity
		
		#modify the flow matrix with current path's flow
		for u,v in path:
			F[idx[u]][idx[v]] += path_flow
			F[idx[v]][idx[u]] -= path_flow
		
			#Create a new residual graph for 6.3
			RG[u][v]['max'] = int(RG[u][v]['max']) - path_flow

		max_flow += path_flow	

	# Print assignments
	assign_task_workers(RG, F, idx)

	return max_flow, F, idx, RG

# Method to print assignments
def assign_task_workers(resultgraph, F, idx):
	file_result.write('\n--- EK 6.2 Assignments: ---\n')
        for x in resultgraph['S']:
                if(x!='TT'):
			file_result.write('\nTask '+x+' -->')
                        for y in resultgraph[x]:
                                if(y!='TT'):
                                        if F[idx[x]][idx[y]] == 1:
						 file_result.write(y+' ')
	file_result.write('\n--- EK 6.2 Assignments ---\n')
	

def main_EK_2():

	t1 = dt.datetime.now()
	
	# Process input
	G = ip.process_input()

	# Modify graph to include super source and sink
	newgraph = mg.modifygraphtodfs(G)

	# Call to edmond-karp algorithm
	max_flow, F, nim, RG = edmond_karp(newgraph,G)

	t2 = dt.datetime.now()

	file_result.write('\nTotal Time Taken to complete 6.2 EK :'+ str((t2-t1).microseconds)+ ' ms\n')

