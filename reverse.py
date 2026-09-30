n = int(input())
s = 0
while n > 0:
    rem = n % 10
    s = s * 10 + rem
    n //= 10
print(s)
