"""
Given an integer array nums, return true if any value appears 
at least twice in the array, and false if all elements are distinct

EXAMPLE 1:
nums = [1,2,3,1]
true

nums = [1,2,3]
false

nums = []
false
"""

# Worst option

# Option 1: Add to dictionary and check if they hit
# this one runs fast!
def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_dict = {}
        for x in nums:
            if x in my_dict.keys(): # checks if x in keys
                return True
            my_dict[x] = 0 # adds key
        return False

"""
Planning:
Worst option: check each element and check the rest of the array: n*(n-1) or O(n^2)
Better: store in dictionary with values as keys. If hits, then true
ALTERNATE: add all to a set, if set size is the same as array size. O(n)

Just with an array: sum array, if it hasn't appeared in one, you'd still have to check every element
"""

