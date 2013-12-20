#!/usr/bin/env python 

#import matplotlib.pyplot as plt
#import networkx as nx
import os

# Method to process input for 6.1 and 6.2
# Process input from text file to python dictionary (graph)
def process_input():

    # Input is transformed to a dictionary 
    graph = {}
    graph[str('S')] = {}
    graph[str('T')] = {}

    file_w = open('inputfile_workers.txt', 'rb')
    file_t = open('inputfile_tasks.txt', 'rb')
    
    count_w = 0
    count_t = 0

    # Process task file
    for i, line in enumerate(file_t):
            if i == 0:
                    count_t = int(line.strip())
            elif i > 0 and i <= count_t:
                    tuple1 = tuple(line.strip().split(','))
            
                    newNode = str(tuple1[0]).strip()
                    graph[newNode] = {}
                    elig = tuple1[3].strip()[1:-1].split(';')
                    
                    graph[str('S')][newNode] = {'min':int(tuple1[1]), 'max':int(tuple1[2])}
                    for e in tuple(elig):
                            graph[newNode][str(e.strip())]= {'min':0, 'max':1} #1
    # Process worker file    
    for i, line in enumerate(file_w):
            if i == 0 :
                    count_w = int(line.strip())
            elif i > 0 and i <= count_w:
                    tuple2 = tuple(line.strip().split(','))
            
                    newNode = tuple2[0].strip()
                    graph[str(newNode)]= {} 
                    graph[str(newNode)][str('T')] = {'min':int(tuple2[1]), 'max':int(tuple2[2])}

    #for k, v in sorted(graph.items()):
    #    print k, graph[k]
    return graph

# Method to process input for 6.3
def process_input_6_3():
    graph = {}
    graph[str('S')] = {}
    graph[str('T')] = {}

    file_t = open('inputfile_6.3.txt', 'rb')
    maxProfit = 0
    count_t = 0

    # Process task file
    for i, line in enumerate(file_t):
        if i == 0:
            count_t = int(line.strip())
        elif i > 0 and i <= count_t:
            tuple1 = tuple(line.strip().split(','))

            newNode = str(tuple1[0]).strip()
            profit = int(tuple1[1])
            pre = tuple1[2].strip()[1:-1].split(';')

            graph[newNode] = {}

            #Create nodes from 'S' and to 'T'
            if profit >= 0:
                maxProfit += profit
                graph[str('S')][newNode] = {'max': profit} #max attribute name- to avoid code changes in draw_graph
            else:
                graph[newNode][str('T')] = {'max': profit * -1}
            
            #If pre is not empty, add dependency edges to the graph
            if len(pre) >=1 and pre[0] != '': 			
                for e in pre:
                    graph[newNode][str(e)]= {'max':float("inf")}

    # Modify 'inf' to a suitable high number- 10 times total profit value
    for n in graph:
        for m in graph[n]:
            if graph[n][m]['max'] == float("inf"):
                graph[n][m]['max'] = int(10 * maxProfit)			
  
    #for k, v in sorted(graph.items()):
    #    print k, graph[k]
    return graph


# Please install networks and matplotlib before uncommenting this method
# After installation, uncomment the imports at the top of thif script
 
# Method to draw graph
#def draw_graph(graph, title):
#    nodes = graph.keys()
#
#    #weighted edges
#    w_edges = []
#    edge_labels = {}
#
#    #Create a directed graph
#    G=nx.DiGraph()
#
#    # Position of nodes
#    posi = {}	
#    i = 0
#    j = 0
#
#    # Create nodes and edges for the directed graph to draw
#    for n in graph.keys():
#	# Position the nodes
#	if n == 'S':
#		posi['S'] = (-0.5,10)
#	elif n == 'T':
#		posi['T'] = (3.5,10)
#	elif n == 'SS':
#		posi['SS'] = (-1,20)
#	elif n == 'TT':
#		posi['TT'] = (4,20)
#	elif n.find('T') != -1:
#		posi[n] = (1, i)
#		i += 5
#	elif n.find('W') != -1:
#		posi[n] = (2, j)
#		j += 5
#
#        G.add_node(n)
#        for e in graph[n]:
#            #wgt = graph[n][e]['max']
#            G.add_edge(n,e)
#            attr_list = {}
#	    if graph[n][e].has_key('min'):
#	            attr_list['min'] =  graph[n][e]['min']
#            attr_list['max'] =  graph[n][e]['max']
#            w_edges.append((n, e, attr_list))
#	    #if graph[n][e].has_key('min'):
#		#edge_labels[(n,e)] = (graph[n][e]['min'], graph[n][e]['max'])
#	    #else:
#	    edge_labels[(n,e)] = graph[n][e]['max']
#
#    G.add_edges_from(w_edges)	
#
#    # For 6.3 : length of dict is 2 with 'S' and 'T' only in posi
#    if len(posi) == 2:
#	pos = nx.circular_layout(G)
#    else:
#	pos = posi
#	
#    #print ('pos', pos)
#    #print ('nodes', nodes)
#
#    # Remove 'S' and 'T' to draw the nodes with different colors
#    nodes.remove('S')
#    nodes.remove('T')
#
#    # Draw nodes
#    nx.draw_networkx_nodes(G,pos,node_size=700, nodelist=['S','T'], node_color='g', label= 'node')
#    nx.draw_networkx_nodes(G,pos,node_size=500, nodelist=sorted(nodes), node_color='b', label= 'node')
#    # If the graph has super source and super sink , draw in different color and size
#    if graph.has_key('SS'):
#	nx.draw_networkx_nodes(G,pos,node_size=900, nodelist=['SS','TT'], node_color='r', label= 'node')
#    
#    # labels
#    nx.draw_networkx_labels(G, pos, font_size=10, font_color='black')
#    # edges
#    nx.draw_networkx_edges(G, pos, width=2, alpha=0.75,edge_color='black', arrows=True)
#   
#    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=0.4)
#    
#    plt.axis('off')
#    
#    plt.savefig(title+".png") # save as png
#    #plt.show() # display


# Method to change graph attributes as the attributes we have used differ for 6.1 and 6.2
def changeGraphAttributes(graph, hasMin, term):
	if term == 'ToCapFlow':	
		newGraph = {}
		for m in graph:
			newGraph[m] = {}
			for n in graph[m]:
				newGraph[m][n] = {}
				newGraph[m][n]['capacity'] = graph[m][n]['max']
				if hasMin:
					newGraph[m][n]['flow'] = graph[m][n]['min']
				else:
					newGraph[m][n]['flow'] = 0
	else:
		newGraph = {}
		for m in graph:
			newGraph[m] = {}
			for n in graph[m]:
				newGraph[m][n] = {}
				newGraph[m][n]['max'] = graph[m][n]['capacity']
				newGraph[m][n]['min'] = graph[m][n]['flow']
	return newGraph

