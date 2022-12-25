'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/882/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "cart"
Output: false
 

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? 
How would you adapt your solution to such a case?
'''
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(f'{s=}, {t=}')
        if len(s)-s.count(' ') != len(t) - t.count(' '):
            return False
        s_chars = []
        for c in s:
            if c == ' ' or c in s_chars:
                continue
            else:
                s_chars.append(c)
            if s.count(c) != t.count(c):
                return False
        return True


c_sol = Solution()
s,t = "anagram", "nagaram"
s,t = "rat", "cart"
s, t = "eleven plus two", "twelve plus one"
s, t = "cheater", "teacher"
s, t = "william shakespeare", "i am a weakish speller"
# s, t = "a", "ab"
out = c_sol.isAnagram(s, t)
print(out)