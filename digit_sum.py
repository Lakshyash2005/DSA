n = int(input())
ans = 0
while n > 0:
    rem = n % 10
    ans += rem
    n //= 10
print(ans)
