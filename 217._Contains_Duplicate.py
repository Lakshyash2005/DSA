# LeetCode 217 - Contains Duplicate
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in nums:
            h[i] = h.get(i, 0) + 1
        for key, val in h.items():
            if val >= 2:
                return True
        return False
