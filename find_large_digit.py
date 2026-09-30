n = int(input())
m = float('-inf')
while n > 0:
    rem = n % 10
    if rem > m:
        m = rem
    n //= 10
print(m)
