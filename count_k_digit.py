n = int(input())
x = int(input("enter the digit to be count:"))
count = 0

while True:
    rem = n % 10
    if rem == x:
        count += 1
    n //= 10
    if n <= 0:
        break

print(count)
