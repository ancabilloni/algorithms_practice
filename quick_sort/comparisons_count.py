"""
Data contains integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the ith row of the file gives you the ith entry of an input array.

Compute the total number of comparisons used to sort the given input file by QuickSort.

Task 1: Use the 1st element of the array as pivot element
Task 2: Use the last element of the array as pivot element
Task 3: Use the median element of the array as pivot element

Approach: use the same partition function, and swap desire pivot element to the first position for pivoting.

"""

def partion(A, l, r):
    p = A[l]
    i = l+1
    for j in range(i,r):
        if A[j] < p:
            swap = A[i]
            A[i] = A[j]
            A[j] = swap
            i += 1
    A[l] = A[i-1]
    A[i-1] = p
    return A, i-1

# Task 1
def quick_sort(A, count=0):
    n = len(A)
    l = 0
    if len(A) <= 1:
        return A, count
    count = count + n - 1
    A, i = partion(A, l, n)
    A[:i], count1 = quick_sort(A[:i], count=count)
    A[i+1:], count2 = quick_sort(A[i+1:], count=count1)
    
    return A, count2

# Task 2
def quick_sort_exchange(A, count=0):
    n = len(A)
    l = 0
    if len(A) <= 1:
        return A, count
    count = count + n - 1
    swap_last = A[n-1]
    A[n-1] = A[0]
    A[0] = swap_last
    A, i = partion(A, l, n)
    A[:i], count1 = quick_sort_exchange(A[:i], count=count)
    A[i+1:], count2 = quick_sort_exchange(A[i+1:], count=count1)
    
    return A, count2

# Task 3
from math import ceil
import numpy as np
            
def quick_sort_median(A, count=0):
    n = len(A)
    l = 0
    if n <= 1:
        return A, count
    
    count = count + n - 1
    # find middle element and median
    mid = ceil(n/2) - 1
    A_mid = A[ceil(n/2) - 1]
    lib = {A[0]: 0, A[mid]: mid, A[n-1]: n-1}
    
    median = np.median([A[0], A[mid], A[n-1]]).astype(int)
    pivot = lib[median]
    
    # swap median to the first
    swap = A[pivot]
    A[pivot] = A[0]
    A[0] = swap
    
    A,i = partion(A, l, n)
    A[:i], count1 = quick_sort_median(A[:i], count=count)
    A[i+1:], count2 = quick_sort_median(A[i+1:], count=count1)
    
    return A, count2

if __name__ == "__main__":
	array = []
	with open('./quick_sort.txt') as fh:
    	for line in fh:
        	array.append(int(line))


    A1, count1 = quick_sort(array)    	
    A2, count2 = quick_sort_exchange(array)
	A3, count3 = quick_sort_median(array)
	
	print ("Task 1: {}".format(count1))
	print ("Task 2: {}".format(count2))
	print ("Task 3: {}".format(count3))



