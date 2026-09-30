i = int(input("enter the days:"))
arr = list(map(int, input().split()))
c = 0
for j in range(i):
    if arr[j] >= 10 and arr[j] % 2 == 0:
        c += 1
print(f"no of productive days: {c}")
