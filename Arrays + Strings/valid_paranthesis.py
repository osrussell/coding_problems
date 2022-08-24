"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the string input is valid

Valid if: Open brackets are closed by the same type of bracket and closed in the correct order

EX1:
Input: s = "()"
Output: true

Input: s = "([{}]())()" 
Ouptut: true

Input: s = ""
Output: true

Input: s = "[(])"
Output: false

Input: "(]"
Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        matching = {')':'(', ']':'[', '}':'{'}
        arr = []
        for x in s:
            if x in matching: # so it's an end paran
                if len(arr) == 0: # checks there is something
                    return False
                match = arr.pop()
                if match != matching[x]:
                    return False
            else: # so forward paran
                arr.append(x)
        if len(arr) == 0:
            return True
        return False

"""
Planning:

Option 1: Put on a queue! Pop on then push off -- this cements order
"""