__author__ = 'bigm141414'
#simple merge sort program in python

#------------------------------------------------------------------------------
unsorted = [2, 4, 7, 1, 5, 6, 3, 0]


def merge_sort(array,n):
    print("Splitting ",array)
    if n < 2:
        print("end of subarray ")

    else:
        print(n)
        print(int(n/2))
        left_half = array[:int(n/2)]
        right_half = array[int(n/2):]

        merge_sort(left_half, int(n/2))
        merge_sort(right_half, int(n/2))
        k = 0
        i=0
        j=0
#------------------------------------------------------------------------------
#  Compare elements in left half vs right half of the recursion.
#  The lowest value will be appended to the output array array[]
#  After comparing all values in one of the arrays the remaining values can
#  be appended since they are the already in sorted order
        while i<len(left_half) and j<len(right_half):
            if left_half[i]< right_half[j]:
                array[k]=left_half[i]
                i+=1
            else:
                array[k]=right_half[j]
                j+=1
            k= k+1

        while i<len(left_half):
            array[k]=left_half[i]
            k+=1
            i+=1
        while j<len(right_half):
            array[k]=right_half[j]
            k+=1
            j+=1
        print(array)
  


final = merge_sort(unsorted, len(unsorted))
print(final)
