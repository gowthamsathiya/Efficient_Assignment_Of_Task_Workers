#!/usr/bin/env python

SetA = []
SetB = []

# Method to compute the min_cut sets
def update_min_cut_sets(G, F, node, nim):
	for v in G[node]:
		if len(v) != 0:
			if F != []:
				residualFlow = G[node][v]['max'] - F[nim[node]][nim[v]]
			else:
				residualFlow = G[node][v]['max']

			if residualFlow > 0 : #reachable
				if v not in SetA:
					SetA.append(v)
					for x in G[v]:
						update_min_cut_sets(G, F, v, nim) #Get all nodes reachable from v
	return SetA

# Method to create min_cut sets
def create_min_cut_sets(G, F, node, nim):
	SetA = update_min_cut_sets(G, F, node, nim)
	SetA.append('S')

	# Include the unreachable nodes to set B
	for key in G.keys():
		if key not in SetA:
			SetB.append(key)

	return set(SetA), set(SetB)

# Method to compute profit and output the reachable tasks
def computeProfit_Output(A, B, G):
	#Compute the total profit by traversing the original graph
	profit = 0
	for m in A:
		if m in A and m != 'S':
			if m in G['S']:
				profit += G['S'][m]['max']
			else:
				if m != 'T':
					profit -= G[m]['T']['max']
	
	setS = set('S')

	# Output the tasks chosen only if profit > 0
	if profit > 0 :
		output = sorted(A - setS)
	else:
		output = 'No profitable tasks available'

	return profit, output
