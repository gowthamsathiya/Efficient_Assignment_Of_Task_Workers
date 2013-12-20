import process_input as pipt
import DFSPath as DFS

# Method to change the attribtues of graph
def changeipt(g):
	newipt = {}
	for x in g:
		newipt[x]={}
		for y in g[x]:
			newipt[x][y] = {}
			newipt[x][y].update({'capacity' : g[x][y]['max']})
			newipt[x][y].update({'flow' : g[x][y]['min']})
	return newipt

# Method to modify the 'flow' and 'capacity' in the graph
def markflow(start,minflowvalue,listsamp,g):
        if listsamp:
                temptuple = listsamp.pop(0)
                g[start][temptuple[0]]['flow']+=minflowvalue
                markflow(temptuple[0],minflowvalue,listsamp,g)

# Method to find min in the path
def findmin(listsamp):
	if listsamp:
		smallestval = float('inf')
		for subset in listsamp:
			smallestval = subset[1] if subset[1] < smallestval else smallestval            
	return smallestval
	
# Method to execute ford fulkerson algorithm
def fordfulkersan(inputgraph):
	
	# DFS call to find a path
        dfspath = DFS.DFSPath(inputgraph)
        path = dfspath.dfs('S','T',[])
        #print("path ",path)

	# Find all paths
        while(path != None):
		minval = findmin(path)
                markflow('S',minval,path,inputgraph)
                dfspath = DFS.DFSPath(inputgraph)
                #print("path1 ",path)
                path = dfspath.dfs('S','T',[])
        return (inputgraph)

# Method to create assignments
def assign_task_workers(inputgraph):
	
	# Modify the attributes of the graph from min-max to cap-flow
	ipt = pipt.changeGraphAttributes(inputgraph, True, 'ToCapFlow')

	#Call to FF algorithm
	resultgraph = fordfulkersan(ipt)

	file_result = open('Result_File_6.1.txt', 'ab')
	file_result.write('\nFF Assignments: \n')

	# Print the assignments
        for x in sorted(resultgraph['S']):
                if(x!='tt'):
                       for y in resultgraph[x]:
                                if(y!='tt'):
                                        if resultgraph[x][y]['flow']!=0:
						file_result.write('Task '+x+' --> '+y+'\n')
	file_result.write('FF Assignments\n')
	return resultgraph

