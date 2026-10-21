# PART 1: Gather Information
#
# I expected this to print the largest number, in this case 17, but it broke
# through a traceback at line 3.
# A traceback error happened, which was a NoneType. I'm guessing because it
# returned type None instead of an integer and broke the function.
# Line 3.


# PART 2: State Assumptions
#
# I assumed it would sort the list for faster lookup, but instead, printing it,
# it returned the type, which is None. Go figure.
# I think it changed the list in place, but I don't know yet.
# Before calling sort, it prints the list, including the values.
# Calling sort without assigning it sorts it instead of returning None.
# Printing list_of_nums after returns the largest number.
# What got thrown away was the list. I thought the list was empty initially,
# so of course it would return None because the list is initially None. No.
# The list started with values. Assigning sort's return value replaced that
# list with None.
# After calling sort without assigning it back, it printed 17.

def get_largest_num(list_of_nums):
    list_of_nums.sort()
    last_index = len(list_of_nums) - 1
    return list_of_nums[last_index]

print(get_largest_num([5, 2, 17, 8, 3]))