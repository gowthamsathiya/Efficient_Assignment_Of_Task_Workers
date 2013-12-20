# Script to execute Fordfulkersan 6.2

import Modifygraph_FF as mg
import DFSPath as DFS
import process_input as ip
import datetime as dt
import os

file_result = open('Result_File_6_2.txt', 'ab')

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
        newgraph = mg.modifygraphtodfs(inputgraph)
        dfspath = DFS.DFSPath(newgraph)
        path = dfspath.dfs('st','tt',[])
        while(path != None):
                minval = findmin(path)
                markflow('st',minval,path,newgraph)
                dfspath = DFS.DFSPath(newgraph)
                path = dfspath.dfs('st','tt',[])
        return (newgraph)

# Method to update the flow in the graph
def minvalueaddition(inputgraph):
        newgraph = fordfulkersan(inputgraph)
        for x in inputgraph:
                for y in inputgraph[x]:
                        newgraph[x][y]['flow']+=inputgraph[x][y]['min']
        return (newgraph)

# Method to create assignments
def assign_task_workers(inputgraph):
        resultgraph = minvalueaddition(inputgraph)
        file_result.write('\n\n--- FF 6.2 Assignments: ---\n')
        for x in resultgraph['S']:
                if(x!='tt'):
                        file_result.write('\nTask '+x+' -->')
                        for y in resultgraph[x]:
                                if(y!='tt'):
                                        if resultgraph[x][y]['flow']!=0:
                                                file_result.write(y+' ')
	file_result.write('\n--- FF 6.2 Assignments ---\n')

# Main method to call Ford -Fulkerson 6.2
def main_FF_2():
	
	t1 = dt.datetime.now()
	inputgraph = ip.process_input()
	assign_task_workers(inputgraph)
	t2 = dt.datetime.now()

	file_result.write('\nTotal Time Taken to complete 6.2 FF :'+ str((t2-t1).microseconds)+ ' ms\n')

