#!/usr/bin/env python 

#import matplotlib.pyplot as plt
#import networkx as nx
import os


# Method to process input for 6.2
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
                            graph[newNode][str(e)]= {'min':0, 'max':1}

    # Process worker file        
    for i, line in enumerate(file_w):
            if i == 0 :
                    count_w = int(line.strip())
            elif i > 0 and i <= count_w:
                    tuple2 = tuple(line.strip().split(','))
            
                    newNode = tuple2[0].strip()
                    graph[str(newNode)]= {} 
                    graph[str(newNode)][str('T')] = {'min':int(tuple2[1]), 'max':int(tuple2[2])}

    # Print the graph
    #for k, v in sorted(graph.items()):
    #    print k, graph[k]
    return graph


# Please install networks and matplotlib before uncommenting this method
# After installation, uncomment the imports at the top of thif script

# Method to draw graph
'''
def draw_graph(graph, title):
    nodes = graph.keys()

    #weighted edges
    w_edges = []
    edge_labels = {}

    #Create a directed graph
    G=nx.DiGraph()

    for n in graph.keys():
        G.add_node(n)
        for e in graph[n]:
            wgt = graph[n][e]['max']
            G.add_edge(n,e)
            attr_list = {}
            attr_list['capacity'] = wgt
            w_edges.append((n, e, attr_list))
            edge_labels[(n,e)] = wgt

    G.add_edges_from(w_edges)	
    #print 'w_edges %s' % w_edges
    #print G.edges(), G.nodes()

    pos=nx.spring_layout(G)
    
    # nodes
    nx.draw_networkx_nodes(G,pos,node_size=500, node_color='b', label= 'node')
    
    # labels
    nx.draw_networkx_labels(G,pos,font_size=10, font_color='black')

    # edges
    nx.draw_networkx_edges(G,pos, width=2,alpha=0.5,edge_color='black')

    #nx.draw(G)
    nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels,label_pos=0.5)
    
    plt.axis('off')
    
    #if not os.path.exists("/Graphs"):
    #	os.makedirs("/Graphs")
    plt.savefig(title+".png") # save as png
    plt.show() # display
    return nx.min_cut(G, 'S', 'T')


graph1 = process_input()
graph2 = process_input_6_3()
draw_graph(graph1, 'graph1')
draw_graph(graph2, 'graph2')
'''
