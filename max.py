def find_max(arr):
    m = float('-inf')
    for x in arr:
        if x > m:
            m = x
    return m

arr = [2, 5, 7, 89, 3, 2]
print(find_max(arr))
