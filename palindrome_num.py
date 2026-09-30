a = int(input())
n = a
s = 0
while n > 0:
    rem = n % 10
    s = s * 10 + rem
    n //= 10

if a == s:
    print(f"{a} is a Palindrome num")
else:
    print(f"{a} is not a Palindrome num")
