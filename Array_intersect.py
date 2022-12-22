'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/674/
Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and 
you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

'''
from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # c = Counter(nums1)
        # print(c)
        common_arr = []
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                common_arr.append(nums1[i])
                i += 1
                j += 1
        return(common_arr)

s = Solution()
nums1, nums2 = [1,2,2,1], [2,2]
# nums1, nums2 = [4,9,5], [9,4,9,8,4]
common_arr = s.intersect(nums1, nums2)
print(f'{common_arr=}')
