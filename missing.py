nums = list(map(int,input("enter the number ").split()))
n = len(nums)

for  i  in range(n+1):
    if i not in nums:
        print(i)