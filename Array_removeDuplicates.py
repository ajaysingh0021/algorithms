'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Test Solution:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

'''
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        filling_counter = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[filling_counter - 1]:
                next
            else:
                nums[filling_counter] = nums[i]
                filling_counter += 1
            nums[i] = "_"
        # nums = nums[:filling_counter]
        return filling_counter

s = Solution()
arr = [0,0,1,1,1,2,2,3,3,4]
k = s.removeDuplicates(arr)
print(k)
print(arr[:k])
print(arr)

print("-" * 30)
# arr = [0,0,1,1,1,2,2,3,3,4]
arr = [-1,0,0,0,3,3]
p = list(set(arr))
p.sort()
k = len(p)
print(k)
print(p)
