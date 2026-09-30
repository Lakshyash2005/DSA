nums = list(map(int, input("enter the number  ").split()))
for i in nums:
    if nums.count(i) == 1:
        print(f"Spy number: {i}, Index: {nums.index(i)}")
        break

    