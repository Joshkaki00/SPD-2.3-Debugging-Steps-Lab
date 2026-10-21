"""
Exercise 1
"""

# PART 1: Gather Information
#
# What I expected was that it was going to print the largest_diff between consecutive
# numbers, but it returns a traceback at line 23 because the index is out of range.
# Traceback at line 23, index out of range. Line 23.
# When I printed the list_of_nums, it returned the entire list values, and I'm
# guessing it's because of this abs(list_of_nums[i] - list_of_nums[i+1]).
# Don't know what that does, and I'm scratching my head.


# PART 2: State Assumptions
#
# i+1 does not always exist. That's why it's crashing and out of range.
# One print is just the indexes, and the other is the index + 1:
# {0} {1} {1} {2} {2} {3} {3} {4} {4} {5}
# I thought the last pair was (5, 6). No. There is no index 6. It's out of range
# of the set. Last valid should be 4, so the last pair is (4, 5).
# I wrote range(len((list_of_nums - 1))), which was wrong syntax and logic.
# It should be range(len(list_of_nums) - 1). Subtract from the length, not the list.
# After that, it printed 4.

def find_largest_diff(list_of_nums):
    """Find the largest difference between *consecutive* numbers in a list."""
    largest_diff = 0
    for i in range(len(list_of_nums) - 1):
        diff = abs(list_of_nums[i] - list_of_nums[i+1])
        if diff > largest_diff:
            largest_diff = diff

    return largest_diff

if __name__ == '__main__':
    print('### Problem 1 ###')
    answer = find_largest_diff([5, 3, 1, 2, 6, 4])

    # This should print 4, as the largest diff between consecutive numbers is between 2 and 6
    print(answer)