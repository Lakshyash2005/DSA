arr = [3, 5, 6, 7, 9, 7, 8, 0, 3, 10]
n = len(arr)

max_val = arr[0]
smax = -1
for i in range(n):
    if max_val < arr[i]:
        smax = max_val
        max_val = arr[i]
print(smax)
