# Script to find DFS

# Class to represent DFS
class DFSPath():
	def __init__(self,gc):
		self.minflow = float("inf")
		self.g = gc

	# Method to find a path using DFS
	def dfs(self,source,sink,path):
		if source == sink:
			return path
		for x in self.g:
			if(x==source):
				for y in self.g[x]:
					cap = self.g[x][y]['capacity']
					flow =self.g[x][y]['flow']
					capacity = cap-flow
					if(capacity > 0 and not (y,capacity) in path):
						self.minflow = capacity if capacity < self.minflow else self.minflow
						res = self.dfs(y,sink,path+[(y,capacity)])
						if res != None:
							return res
						    
