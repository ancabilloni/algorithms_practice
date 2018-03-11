#! /usr/bin/evn python

"""
Description: implement Dijkstra to find the shortest-path for all vertices of a given un-directed graph.
Optional challenge: apply heap-based version.

Run-time:
Naive: O(mn)
Heap-based: O(log(n))

# Required vertices for shortest-path: 7,37,59,82,99,115,133,165,188,197

"""

from heapq import *

# Loading data object
class loadFile(object):

	def __init__(self, filename):
		self.data = [0]

		with open(filename, 'r') as fh:
			for line in fh:
				a = [int(line.split()[0])] + [a.split(',') for a in line.split()[1:]]
				self.data.append(a)
			self.max_vertice = self.data[-1][0]

# Dijkstra algorithm object
class Dijkstra(loadFile):
	def __init__(self,filename, required_vertices_output):
		super(Dijkstra, self).__init__(filename)
		self.visited = []
		self.distance = [float('inf')]*(self.max_vertice+1)
		self.require_output = required_vertices_output

	def dijkstra(self):
		self.distance[1] = 0 # since source node is at vertices 1, its distance == 0.
		self.heap = [(0,1)] # (distance, vertices)

		while self.heap:
			current_min = heappop(self.heap)[1] # min of heap is selected for exploration
			self.visited.append(current_min) # min of heap is the best min distance for that node.

			for edge in self.data[current_min][1:]:
				v, e = int(edge[0]), int(edge[1])

				if v not in self.visited:
					 dist = self.distance[current_min] + e

					 if dist < self.distance[v]: # if new distance is less than previous distance, udpate.
					 	self.distance[v] = dist
					 	heappush(self.heap, (dist, v))

		return [self.distance[x] for x in self.require_output]

if __name__ == "__main__":
	# Test Case
	filename = './dijkstra/input_random_1_4.txt'
	result = './dijkstra/output_random_1_4.txt'
	required_output = [7,37,59,82,99,115,133,165,188,197] # Showing shortest path distances for these vertices

	test_data = Dijkstra(filename, required_output)
	test_result = test_data.dijkstra()

	output_result = []
	with open(result, 'r') as fh:
		for line in fh:
			output_result = [int(x) for x in line.split(',')]


	print ('Dijkstra result: ', test_result)
	print ('Output result:   ', output_result)
	print ('The result is: ', test_result == output_result)

	# Actual Data
	filename = './dijkstraData.txt'
	test_data = Dijkstra(filename, required_output)
	test_result = test_data.dijkstra()

	print ('Result: ', test_result)
	# Correct Result: 2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068


