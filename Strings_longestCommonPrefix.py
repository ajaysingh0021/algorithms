'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/887/

Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # print(strs)
        out = []
        a = []
        min_len = len(min(strs, key=len))
        # print(min_len)
        for i in range(min_len):
            for list in strs:
                a.append(list[i])
            # print(f'{a=}')
            if len(set(a)) > 1:
                break
            else:
                out.append(a.pop())
            a = []
        return "".join(out)


s = Solution()
strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
out = s.longestCommonPrefix(strs)
print(out)