#Script to modify input graph by adding st and tt

def modifygraphtodfs(graph):
	newgraph = {}
	newgraph['st'] = {}
	for x in graph:
		newgraph[x] = {}
		sumofminoutflow = 0
		for y in graph[x]:
			newgraph[x][y] = {}
			sumofminoutflow+=graph[x][y]['min']
			newgraph[x][y].update({'capacity' : graph[x][y]['max'] - graph[x][y]['min']})
			newgraph[x][y].update({'flow' : 0})
			newgraph['st'][y] = {'capacity' : (newgraph['st'][y]['capacity'] if newgraph['st'].get(y) != None else 0) + graph[x][y]['min']}
			newgraph['st'][y].update({'flow' : 0})
		newgraph[x]['tt']={}	
		newgraph[x]['tt'] = {'capacity' : sumofminoutflow}
		newgraph[x]['tt'].update({'flow' : 0})
	newgraph['T']={}
	newgraph['T']['S']={}
	newgraph['T']['S'].update({'capacity' : 100})
	newgraph['T']['S'].update({'flow' : 0})
	return newgraph
