n = int(input())
arr = list(map(int,input().split()))
arr.sort(reverse=True)
total = sum(arr)
my_sum = 0
count = 0 

for coin in arr:
    my_sum += coin 
    count += 1

    if my_sum >total - my_sum:
        break 
    print(count )

# -------- Move Zeroes to End (LeetCode 283) --------
# Two-pointer (in-place, O(n) time, O(1) space)
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        j = 0  # pointer for the next non-zero position
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
