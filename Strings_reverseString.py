'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/879/

Reverse String
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


'''
from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
    
    def reverseString_withExtraVar(self, s: List[str]) -> None:
        out = []
        while s:
            out.append(s.pop())
        print(out)

sol = Solution()
s = ["H","a","n","n","a","h"]
s = ["h","e","l","l","o"]
sol.reverseString(s)

sol.reverseString_withExtraVar(s)

# print(s)


