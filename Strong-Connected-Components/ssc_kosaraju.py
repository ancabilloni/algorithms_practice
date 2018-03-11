# /usr/bin/env/python

"""
This is the implementation of KOSARAJU to find the maximum number of 
Strong Connected Components.

The algorithm requires 2 passes. The first one is to loop through the vertices
in reverse to find the run time of each vertices.
Then, there is a required re-map to point the nodes to its running time accordingly,
then point backward to its the nodes in its original setup.
The second pass will be looped through the same as the first pass.

"""
import os
from collections import defaultdict
import sys
import time

class loadData(object):
	def __init__(self, filename):
		self.data = defaultdict(list)
		# try:
		# 	with open(filename) as fh:
		# 		pass
		# except IOError:
		# 	raise IOError('Re-check on input path. The current input path does not exist.')

		if os.path.isfile(filename):
			with open(filename, 'r') as fh:
				for line in fh:
					[u, v] = [int(x) for x in line.split()]
					self.data[u].append(v)
		else:
			for line in filename:
				u, v = line[0], line[1]
				self.data[u].append(v)


class SCC(loadData):
	def __init__(self, filename):
		super(SCC, self).__init__(filename)
		self.t = 0
		self.s = 0
		self.vertices = list(self.data.keys())[-1]
		self.explored = [False]*self.vertices
		self.finish_time = [0]*self.vertices
		self.leaders = [0]*self.vertices
		self.count = dict((key, 0) for key in range(1,self.vertices+1))
		
	def reset(self):
		self.explored = [False]*self.vertices
		self.finish_time = [0]*self.vertices


	def graphReverse(self):
		self.graph = defaultdict(list)

		for u,v in self.data.items():
			update_u = self.finish_time[u-1]
			for vertice in v:
				update_v = self.finish_time[vertice-1]
				self.graph[update_v].append(update_u)
		self.reset()


	def DFS_firstPass(self, graph, i):
		self.explored[i-1] = True

		for j in graph[i]:
			if not self.explored[j-1]:
				self.DFS_firstPass(graph, j)

		self.t += 1
		self.finish_time[i-1] = self.t

	def DFS_secondPass(self, graph, i):
		self.explored[i-1] = True
		self.leaders[i-1] = self.s
		self.count[self.s] += 1

		for j in graph[i]:
			if not self.explored[j-1]:
				self.DFS_secondPass(graph, j)

	def DFS_loop(self):
		# First pass
		for i in range(self.vertices,0,-1):
			if not self.explored[i-1]:
				self.DFS_firstPass(self.data, i)

		# Reset required variables for 2nd pass and re-map graph.
		self.graphReverse()

		# Second Pass

		for i in range(self.vertices,-1,-1):
			if not self.explored[i-1]:
				self.s = i 
				self.DFS_secondPass(self.graph, i)

		max_count = sorted(self.count.values(), reverse=True)[:5]

		return max_count

if __name__ == '__main__':
	sys.setrecursionlimit(4000000) # increase recursion limit
	filename = './SCC.txt'
	time_in = time.time()
	scc = SCC(filename)
	max_scc = scc.DFS_loop()
	print (max_scc)
	out = time.time()
	print ('Total time: {} seconds'.format(out - time_in))

	# type 'ulimit -s 65532' on terminal to increase stack size












