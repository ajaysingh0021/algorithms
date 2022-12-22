'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/567/
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

'''

# arr = [0,2,0,5,18]
# n = len(arr)
# k = arr.count(0)
# print(k)
# for _ in range(k):
#     arr.remove(0)
# print(arr)
# for _ in range(k):
#     arr.append(0)
# print(arr)

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
        
s = Solution()
nums = [0,1,0,3,12]
# nums = [0]
s.moveZeroes(nums)
print(nums)