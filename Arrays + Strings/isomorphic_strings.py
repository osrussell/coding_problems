"""
Given two strings s and t, determine if they are isomorphic (characters in s can be replaced to get t)
All occurrences of a character must be replaced with another character while preserving order.
No two characters may map to the same character, but a character can map to itself.

EX 1:
Input: s = "eggd", t = "addo"
Ouput: True

EX 2:
Input s = "foo", t = "bar" 
Output: False

EX 3:
Input s = "a", t = "b"
Output: True

EX 4:
Input s = "ab", t = "cc"
Output: False
"""

# Non-optimal solution both speed and memory wise
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        my_dict = {}
        has_mapping = {}
        new_s = ""
        for i in range(len(s)): # both strings have the same length
            if s[i] in my_dict: # if letter has been seen before
                if not (my_dict[s[i]] == t[i]): # checks if mapping doesn't match t
                    return False
            else: # if letter is new
                if t[i] in has_mapping:
                    return False
                my_dict[s[i]] = t[i]
                has_mapping[t[i]] = ""
            new_s += t[i]
        
        if new_s == t:
            return True
        return False

"""
Planning!
We're mapping unique elements. Could just replace first new letter we see with next number, and then see if final numbers are the same

Option 1: For each string, loop through the letters. If letter has been seen before, 

Option 2: Loop through both strings. Check first string and match to character in second
If letter has been seen before, switch to val from dictionary.
If it hasn't been seen before, add to dictionary with value from other string
Can auto end if seen before, and val from dictionary doesn't match 
"""