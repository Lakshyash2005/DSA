# LeetCode 268 - Missing Number
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s ^= nums[i]
            s ^= i
        s ^= len(nums)
        return s
