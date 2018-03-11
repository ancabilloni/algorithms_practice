"""
Given a sorted list with sub-list. If the list range overlapped, merge the list.

"""

def merge_ranges(input_range_list):
    merge = []
    var = input_range_list[0]
    n = len(input_range_list)
    for i in range(n):
        if input_range_list[i][0] <= var[1]:
            var[1] = input_range_list[i][1]
        else:
            merge.append(var)
            var = input_range_list[i]
    
    if var[0] > merge[-1][1]:
        merge.append(var)
        
    return merge
    
print(merge_ranges([[1,4], [3,7], [5,10], [11,15]])) #[[1,10], [11,15]]
print (merge_ranges([[1,2], [2,5], [8,10], [15,20]])) #[[1,5], [8,10], [15,20]]
