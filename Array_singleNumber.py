'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/549/

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

'''
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        map_num = {}
        for i in nums:
            if map_num.get(i, 0):
                map_num[i] += 1
            else:
                map_num[i] = 1
        # print(map_num)
        for k,v in map_num.items():
            if v == 1:
                return k
                
s = Solution()
nums = [2,2,1]
# nums = [4,1,2,1,2]
nums = [1]
k = s.singleNumber(nums)
print(k)
