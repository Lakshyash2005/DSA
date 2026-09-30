# LeetCode 283 - Move Zeroes
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        i, j = 1, 0
        while i < n and j < n:
            if nums[j] != 0:
                j += 1
            elif nums[i] != 0 and j < i:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1
