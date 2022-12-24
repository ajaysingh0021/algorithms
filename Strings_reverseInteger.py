'''
https://leetcode.com/explore/featured/card/top-interview-questions-easy/127/strings/880/

Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

'''

class Solution:
    def reverse(self, x: int) -> int:
        sum = 0
        sign = 1
        if x < 0:
            sign = -1
            x = x * sign
        while x > 0:
            n = x % 10
            sum = sum*10 + n
            x = x // 10
        if not -pow(2, 31) < sum < pow(2, 31) - 1:
            return 0
        return sum*sign

    def reverse2(self, x: int) -> int:
        if x == 0: return 0
        out = []
        t = [c for c in str(x)]
        t.reverse()
        # print(t)
        nonZeroStart = False
        for c in t:
            if c == "0" and nonZeroStart == False:
                continue
            else:
                nonZeroStart = True
            out.append(c)
        # print(out)
        if out[-1] == "-":
            out.pop()
            out.insert(0, "-")
        p = int("".join(out))
        if p > pow(2,31) - 1 or p < -pow(2,31):
            return 0
        return p

s = Solution()
x = 1534236469
x = 0
# x = -1230
print(f"Main String = {x}")
out = s.reverse(x)
print(f"Reverse string = {out}")