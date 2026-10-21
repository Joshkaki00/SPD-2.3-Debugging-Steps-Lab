"""
Exercise 4
"""

# PART 1: Gather Information
#
# I expected this to do a binary search, but it crashed at line 22 from an indentation error.
# A traceback at line 22, indentation error.
# Line 22.
# I can deduce that the indentation needs to be fixed before running the rest of the loop.
#
# After that, I expected this to do a binary search, but it crashed at line 37 with a traceback.
# Traceback error at line 37, maximum recursion depth exceeded.
# Yes, at line 37.
# I can deduce that the loop runs past the maximum depth of the tree traversal, and that is why this crashes.


# PART 2: State Assumptions
#
# HINT: It may help to draw a picture to clarify what your assumptions are.
#
# They keep repeating until the end of the tree and crash. It stuck on 3 3 4.
# low and mid were both 3, and that index holds 5, which is smaller than 7.
# The else called again with low set to mid, so the next low was still 3.
# The next low should be index 4, one past mid.
# I changed it to look before the mid if arr[mid] is greater than the element, else look after it.
# When arr[mid] is greater, the new high is mid - 1 and low stays.
# In the else, the new low is mid + 1 and high stays.
# Then it printed 4.

def binary_search(arr, element, low=0, high=None):
    """Returns the index of the given element within the array by performing a binary search."""
    if high == None:
        high = len(arr) - 1

    if high < low:
        return -1

    mid = (high + low) // 2

    if arr[mid] == element:
        return mid

    elif arr[mid] > element:
        return binary_search(arr, element, low, mid - 1)

    else:
        return binary_search(arr, element, mid + 1, high)


if __name__ == '__main__':
    answer = binary_search([1, 2, 4, 5, 7], 7)
    print(answer)