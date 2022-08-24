"""
Given a string s, reverse only all the vowels in the string and return it

EX 1:
Input: s = "hello"
Output: "holle"

Input: "leetcode"
Ouput: "leotcede"

Input: ""
Output: ""
"""

#done with a queue
# runtime faster than 81% python
# memory less than 97% of python
class Solution:
    def reverseVowels(self, s: str) -> str:
        my_dict = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
        q = []
        for x in s:
            if x in my_dict: # if it's a vowel
                q.append()
        
        new_s = ""
        for x in s:
            if x in my_dict: # if it's a vowel
                new_s = new_s + q.pop()
            else:
                new_s = new_s + x
        return new_s

#done with pointers

"""
Planning:

Option 1: take every vowel and put on queue?? then pop back off 
Currently though, first we need to go through n to put everything on, then pop back off 
So probably O(n)
This requires checking if vowel for everything in dictionary though, and then doing it AGAIN as we re-assemble
"""