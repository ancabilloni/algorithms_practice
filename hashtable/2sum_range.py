#! /usr/bin/en python
"""
Given a range of target numbers [-x, x] and input array A (1 millions input with some repeating values) 
in unsorted order. There can be exactly one
distinct pair (a,b) numbers in the given array that its sum equals to a number in the given range.

Find one distinct pair (a,b) for each target value if they exists. Provide the output of total
number of targets have existing sum.

Solution:
- Sort array and remove repeatition. 
- Define lower and upper bound of available values for each value in given input.
hashmap = [0]*(2*x + 1)
For value in A;
	lower_bound = neareast index to (-x - value)
	upper_bound = nearest index to (x - value)

	chosen_range = A[lower_bound:upper_bound] 
	if chosen_range is not empty:
		found_sum_range = chosen_range + value
		update hashmap[found_sum_range] = 1

total_count = sum(hashmap)

"""

class loadData(object):
    def __init__(self, filename):
        self.data = []
        self.org_data = []
        with open(filename, 'r') as fh:
            for line in fh:
                self.org_data.append(int(line))
            self.org_data = list(set(self.org_data))

from bisect import *
import numpy as np

class twoSum:
	def __init__(self, filename, range):
		self.data = sorted(loadData(filename).org_data)
		self.range = range
		self.total = 0

	def findtotalSum(self):
		print ("Start counting...")
		for target in range(self.range[0], self.range[1]+1):

			if ((self.data[-1] + self.data[-2]) < target) or ((self.data[0] + self.data[1]) > target):
				found = 0			
			else:
				found = self._findtotalSum(target, self.data)
			self.total += found

		print ("Total sum found: ", self.total)

	def biSectMethod(self):
		target_check = np.array([0]*200001)
		target = [x for x in range(self.range[0], self.range[1]+1)]

		for v in self.data:

			if len(target) == 0:
				break
			
			l = self.range[0] - v
			r = self.range[1] - v

			lower = bisect(self.data, l)
			higher = bisect(self.data, r)

			chosen_arr = self.data[lower:higher]

			if chosen_arr != []:
				array = np.array(chosen_arr) + v 
				target_check[array] = 1

		print ("Total count: {} ".format(sum(target_check)))

if __name__ == '__main__':
	filename = './hashtables/2sum.txt'
	range_target = [-10000,10000]
	twosum = twoSum(filename, range_target)
	twosum.biSectMethod()
	#answer: 427