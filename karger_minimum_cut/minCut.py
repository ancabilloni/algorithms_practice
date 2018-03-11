"""
Given the file contains the adjacency list representation of an undirected graph. There are
200 vertices labeled 1 to 200. For each row, the first column is the vertex label, and rest of the entries are the adjacent vertices.

Task: Code and run the randomized contraction algorithm to compute the min cut for the graph.

"""
class loadData(object):
    def __init__(self, filename):
        self.data = []
        self.org_data = []
        with open(filename, 'r') as fh:
            for line in fh:
                self.org_data.append([int(x) for x in line.split()])

import random

class minCut(loadData):
    
    def partion(self, array, l, r):
        p = array[l]
        i = l+1
        for j in range(l+1, r):
            if array[j] < p:
                swap = array[j]
                array[j] = array[i]
                array[i] = swap
                i += 1
        array[l] = array[i-1]
        array[i-1] = p
        return array, i-1
        
    def findElementIndex(self, array, element):
        for j in range(len(array)):
            if array[j] == element:
                return j
        return None
            
    def updateArray(self, array, element):
        index = self.findElementIndex(array, element)
        if index is not None:
            array = array[:index] + array[index+1:]
            return array
        return None
    
    def min_cut(self):
        data = self.org_data[:]
        # print (self.org_data)
        n = len(data)
        min_cut = 0
        # print (data[0])

        vertices = [x for x in range(n)]

        while n > 2:
            # pick a random vertex index
            i = vertices[random.randint(0, len(vertices)-1)]
                
            # pick a random edge connected to contract
            i_contracted = random.randint(1,len(data[i]) - 1)
            _contractedNode = data[i][i_contracted]
            
            # Remove contractedNode and Update chosen vertex
            # Remove self-loop
            self_loop = True
            while self_loop:
                temp_array_i = self.updateArray(data[i], _contractedNode)
                temp_array_contracted = self.updateArray(data[_contractedNode-1], i+1)
                if temp_array_i is not None:
                    data[i] = temp_array_i
                    data[_contractedNode-1] = temp_array_contracted
                else:
                    self_loop = False
            
            # Remove chosen vertex in contractedNode
            data[i] = data[i] + data[_contractedNode-1][1:]
            
            
            for vertex in data[_contractedNode-1][1:]:
                data[vertex-1] = self.updateArray(data[vertex-1], _contractedNode)
                data[vertex-1].append(i+1)
            
            data[_contractedNode-1] = []

            remove_vertex_ind = self.findElementIndex(vertices, _contractedNode-1)
            vertices = vertices[:remove_vertex_ind] + vertices[remove_vertex_ind+1:]
            # print ("after: ", vertices)

            n = n - 1

        min_cut = len(data[vertices[0]]) - 1

        return min_cut
    
    def minCutLoop(self, num_of_loop):
        minCut = 10000
        list_min =[]
        for i in range(num_of_loop):
            trial_cut = self.min_cut()
            if minCut > trial_cut:
                minCut = trial_cut
                list_min.append(minCut)
        return minCut, list_min
            
if __name__ == "__main__":
	filename = "./kargerMinCut.txt"
	# filename = './input_random_10_25.txt'
	data = minCut(filename)

	list_min_cut =[]

	min_cut, list_min_cut = data.minCutLoop(100)
	# list_min_cut.append(min_cut)
	print (list_min_cut)
	print (); print (min_cut)
