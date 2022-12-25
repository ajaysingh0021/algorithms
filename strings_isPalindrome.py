'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/883/

Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(f'{s=}')
        t = []
        for c in s:
            if c.isalnum():
                t.append(c)
        x = "".join(t).lower()
        y = x[::-1]
        print(f'{x=} {y=}')
        if x != y:
            return False
        return True


c_class = Solution()
s = " "
s = "A man, a plan, a canal: Panama"
# s = "race a car"
out = c_class.isPalindrome(s)
print(out)
