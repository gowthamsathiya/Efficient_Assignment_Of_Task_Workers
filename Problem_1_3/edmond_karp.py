#!/usr/bin/env python 

import process_input as ip
import BFS
import os

file_result = None

def edmond_karp(G, probNum, origGraph):
	
	# Flow matrix to keep track of residual and used capacities
	n = len(G.keys()) #number of nodes
	F = [[0] * n for i in xrange(n)] #Flow, reverse edges 
	
	#create key-value pairs for nodes and Flow matrix idx
	idx = {} #node_idx_map
	for i, node in enumerate(G.keys()):	
		idx[node] = int(i)

	max_flow = 0
	RG = G

	# Update the flow matrix with minimum assumed flow
	if origGraph is not None:
		#print 'Orig Graph:'
		#for k, v in sorted(origGraph.items()):
        	#	print k, origGraph[k]

		for x in origGraph:
			for y in origGraph[x]:
				minval = origGraph[x][y]['min']
				F[idx[x]][idx[y]] = minval
		 
	
	#Find all paths using BFS
	while True:
		if origGraph is not None:
			path = BFS.bfs(G, F, 'SS', 'TT', idx)
			# print 'path: %s' % path
		else: 
			path = BFS.bfs(G, F, 'S', 'T', idx)
	 	
		if not path: 
			break

		#compute flow allowable for the current path
		path_flow = min(G[u][v]['max'] - F[idx[u]][idx[v]] for u,v in path) #Total Capacity - used capacity
		
		#modify the flow matrix with current path's flow
		for u,v in path:
			F[idx[u]][idx[v]] += path_flow
			F[idx[v]][idx[u]] -= path_flow

			#Create a new residual graph to output assignments
			RG[u][v]['max'] = int(RG[u][v]['max']) - path_flow

		max_flow += path_flow
		#print 'path: '
		#print path, path_flow, F

	#Print assignemnts only if its not 6.3
	if probNum != '6.3':
		file_result = open('Result_File_6.1.txt', 'ab')
		assign_task_workers(RG, file_result)

	return max_flow, F, idx, RG
	
# Method to print assignments
def assign_task_workers(resultgraph, file_result):
	file_result.write('\nEK Assignments: \n')
	
	# Print the assignments
        for x in sorted(resultgraph['S']):
                if(x!='TT'):
                        for y in resultgraph[x]:
                                if(y!='TT'):
                                        if resultgraph[x][y]['max']==0:
						file_result.write('Task '+x+' --> '+y+'\n')
	file_result.write('EK Assignments \n')

