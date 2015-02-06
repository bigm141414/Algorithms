__author__ = 'bigm141414'
#simple merge sort program in python

#------------------------------------------------------------------------------
unsorted = [2, 4, 7, 2, 1, 5, 6, 3, 0]

def merge_sort(array,n):
    if n < 2:
        print("end of subarray ")
        return array
    else:
        left_half = array[:n/2]
        right_half = array[n/2:]
        merge_sort(left_half,n/2)
        merge_sort(right_half,n/2)
    c = []
    k = 0
    for i in range(len(left_half)) and range(len(right_half)):
        if left_half[i] > right_half[i]:
            c.append(right_half[i])
    return c




final = merge_sort(unsorted,len(unsorted))
print(final)



