"""
Exercise 3
"""

# PART 1: Gather Information
#
# I expected this to print the sorted set, but it crashed and went through a traceback.
# Yes, traceback at line 26, index out of range.
# Line 26.
# I deduced from printing that j tries to look for a range of 6 even though there
# are only 5 values in the set, so it is already out of range. It's probably the
# assignment that's messing it up.


# PART 2: State Assumptions
#
# HINT: It may help to draw a picture to clarify what your assumptions are.
#
# Index goes below 0. Valid indexes are only 0 through 4.
# I changed while key < arr[j] to while j >= 0 and key < arr[j] so that it doesn't
# go below 0 and sorts the set.
# Then it printed [1, 2, 3, 5, 6].

def insertion_sort(arr):
    """Performs an Insertion Sort on the array arr."""
    for i in range(1, len(arr)):
        key = arr[i] 

        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key
        
    return arr

if __name__ == '__main__':
    print('### Problem 3 ###')
    answer = insertion_sort([5, 2, 3, 1, 6])
    print(answer)

