n = int(input())
ar = list(map(int, input().split()))

for i in range(n):
    a = ar[i]
    arr = []
    c = 1
    count = 0
    while a > 0:
        r = a % 10
        if r != 0:
            r *= c
            arr.append(r)
            count += 1
        c *= 10
        a //= 10
    print()
    print(count)
    print(*arr)
