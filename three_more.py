i = int(input())
arr = list(map(int, input().split()))
c = 0
for j in range(1, i):
    if arr[j - 1] <= arr[j] - 3:
        c += 1
print(f"no. of improvement days:{c}")
