#! /usr/bin/en python
"""
Given a file of integers from 1 to 10000 in unsorted order in streaming order arriving one by
one. Letting x_i denote the ith number of the file, the kth median m_k is defined as the median of the numbers x1,...,xk. So, if k is odd, then m_k is ((k+1)/2)th smallest.
If k is even, then m_k is the k/2 th smallest number among x1,...,xk.

Find the sume of all 10000 medians, modulo 10000.
"""

from heapq import *
import time

class loadData(object):
    def __init__(self, filename):
        self.data = []
        self.org_data = []
        with open(filename, 'r') as fh:
            for line in fh:
                self.org_data.append(int(line))

# Built-in min heap function
class median(loadData):

	def findTotalMedian(self):
		total = 0
		m_k = []
		current_arr = []

		for i in range(1, len(self.org_data)+1):
			k = int((i+1)/2)
			current_arr.append(self.org_data[i-1])
			# heap = heapify(current_arr)
			m_k = nsmallest(k, current_arr)[-1]

			total = (total + m_k)
		return total %10000

# BTS Search
class node():
	def __init__(self, value):
		self.value = value
		self.left_child = None
		self.left_child_number = None
		self.right_child = None
		self.right_child_number = None
		self.size = 1

class binary_tree():
	def __init__(self,value=None):
		self.root = None

	def insert(self, value):
		if self.root == None:
			self.root = node(value)
		else:
			self._insert(value, self.root)

	def _insert(self, value, cur_node):
		if value < cur_node.value:
			if cur_node.left_child == None:
				cur_node.left_child = node(value)
				cur_node.size += 1
			else:
				self._insert(value, cur_node.left_child)
		elif value > cur_node.value:
			if cur_node.right_child == None:
				cur_node.right_child = node(value)
				cur_node.size += 1
			else:
				self._insert(value, cur_node.right_child)

	def get_k_min(self, k):
		k_min_elements = []
		if self.root != None:
			self._get_k_min(self.root, k_min_elements, k)
		
		return k_min_elements[-1]

	def _get_k_min(self, cur_node, k_array, k):
		if cur_node != None and len(k_array) < k:
			self._get_k_min(cur_node.left_child, k_array, k)
			if len(k_array) < k:
				k_array.append(cur_node.value)
				self._get_k_min(cur_node.right_child, k_array, k)


def findMedian(array):
	tree = binary_tree()
	m_k = 0
	for i in range(1, len(array)+1):
		median = int((i+1)/2)
		tree.insert(array[i-1])
		m_k = (m_k + tree.get_k_min(median))

	return (m_k%10000)


if __name__ == "__main__":
	filename = './BTS/Median.txt'

	start = time.time()
	data = median(filename)
	value = data.findTotalMedian()
	stop = time.time()
	print ('Using min heap built-in method takes {} seconds'.format(stop-start))
	print (value)

	print ();


	start = time.time()
	data = loadData(filename)
	value2 = findMedian(data.org_data)
	stop = time.time()
	print ('Using binary unbalance tree method takes {} seconds'.format(stop-start))
	print (value2)






