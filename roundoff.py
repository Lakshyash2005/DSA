def solve():
    n = int(input("enter the number "))
    terms= []
    power = 1 
    while n > 0:
        digit =n%10
        if digit != 0:
            terms.append(digit*power)
        n //= 10
        power *= 10
    print(len(terms))
    print(*terms)
solve()
