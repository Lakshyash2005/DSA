n = int(input())
arr1 = list(map(int, input().split()))
arr2 = []
for x in arr1:
    if x > 0:
        arr2.append(x)
for x in arr1:
    if x == 0:
        arr2.append(x)
print(*arr2)
