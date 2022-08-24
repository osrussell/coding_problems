"""
Given an array nums and an input target, return indices that add to target.
There is exactly one solution and you can't use the same number twice

EX1:
nums = [2,7,11,15]
target = 9
output = [0,1]
"""

# Option 4
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for x in range(len(nums)): # we need the indices later
            rest = target - nums[x]
            if rest in my_dict:
                # print(x)
                return [my_dict[rest], x]
            else:
                my_dict[nums[x]] = x


"""
Planning

Worst: check all of first array for anything in the second, and then you have to remove

Option 1: SORT! this cuts down on some by excluding too large

Option 2: store in a dictionary

Option 3: Sort, then until you reach target/2 value store in dictionary, where other val is index in array. Then see if rest until target value have val in dictionary
This is O(n*logn)

Option 4: Each item goes into a dictionary after checking if their opposite key is there. If yes, return spots, if not, add. Index is stored 
"""