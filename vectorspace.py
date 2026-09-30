n = int(input())
xf = 0
yf = 0
zf = 0
for _ in range(n):
    x, y, z = map(int, input().split())
    xf += x
    yf += y
    zf += z

if xf != 0 or yf != 0 or zf != 0:
    print("NO")
else:
    print("YES")
