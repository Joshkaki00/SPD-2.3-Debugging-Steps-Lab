"""
Exercise 2
"""

# PART 1: Gather Information
#
# I expected each call to print True for the second, since there are 3
# consecutive numbers, but no. It's false.
# No crash. It's a logic error.
# No traceback.
# Logic error somehow. Probably the return False in the else is going to return
# false regardless and makes both the if and True outputs false.


# PART 2: State Assumptions
#
# Printed this:
# 0 1 2 4
# False
# 0 4 1 2
# I'm not seeing the last number for ans2. Is that why?
# It seemed like both start at values 0 instead of index 0. Nope, that 0 is
# the index. First window of the second list is 4, 1, 2.
# It does not keep going. It should not stop. It should keep checking until
# it's either true or false.
# Took out the else return False. Then it also printed:
# 1 1 2 3
# True

def contains_3_consecutive(list_of_nums):
    """Return True if the list contains 3 consecutive numbers each increasing by 1."""
    
    for i in range(len(list_of_nums) - 2):
        if (list_of_nums[i+1] == list_of_nums[i] + 1 and
            list_of_nums[i+2] == list_of_nums[i] + 2):
            return True

    return False

if __name__ == '__main__':
    print('### Problem 2 ###')
    answer1 = contains_3_consecutive([1, 2, 4])
    print(answer1) # should print False

    answer2 = contains_3_consecutive([4, 1, 2, 3])
    print(answer2) # should print True