n = int(input())
arr = list(map(int, input().split()))
ans = 0
h = {}
for x in arr:
    h[x] = h.get(x, 0) + 1
for key, val in h.items():
    if val == 1:
        ans = key
for i in range(n):
    if arr[i] == ans:
        print(i + 1)
        break
