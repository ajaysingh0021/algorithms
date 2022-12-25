'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/881/

First Unique Character in a String
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
'''
from typing import List 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1

s_class = Solution()
s = "leetcode"
# s = "loveleetcode"
# s = "aabb"
out = s_class.firstUniqChar(s)
print(out)


