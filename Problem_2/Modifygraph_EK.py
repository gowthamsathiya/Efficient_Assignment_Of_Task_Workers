#Script to modify input graph by adding st and tt

# Method to modify the graph to contain super source, super sink and circulation edge
def modifygraphtodfs(graph):
	newgraph = {}
	newgraph['SS'] = {}
	newgraph['TT'] = {}
	for x in graph:
		newgraph[x] = {}
		sumofminoutflow = 0
		for y in graph[x]:
			newgraph[x][y] = {}
			sumofminoutflow+=graph[x][y]['min']
			newgraph[x][y].update({'max' : graph[x][y]['max'] - graph[x][y]['min']})
			newgraph[x][y].update({'min' : 0})
			newgraph['SS'][y] = {'max' : (newgraph['SS'][y]['max'] if newgraph['SS'].get(y) != None else 0) + graph[x][y]['min']}
			newgraph['SS'][y].update({'min' : 0})
		newgraph[x]['TT']={}	
		newgraph[x]['TT'] = {'max' : sumofminoutflow}
		newgraph[x]['TT'].update({'min' : 0})

	# Add the circulation edge from 'T' to 'S'
	newgraph['T']={}
	newgraph['T']['S']={}
	newgraph['T']['S'].update({'max' : 10000})
	newgraph['T']['S'].update({'min' : 0})
	return newgraph
