n = int(input())
count = 0

for i in range(1, n + 1):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if flag:
        count += 1

print(f"composite:{count} prime:{n - count}")
