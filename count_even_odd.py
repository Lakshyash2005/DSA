n = int(input())
even = 0
odd = 0

while True:
    rem = n % 10
    if rem % 2 == 0:
        even += 1
    else:
        odd += 1
    n //= 10
    if n <= 0:
        break

print(f"even count:{even}")
print(f"odd count:{odd}")
