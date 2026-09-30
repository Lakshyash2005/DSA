arr= [3,5,6,7,8,9,10]

max_val = arr[0]
min_val = arr[0]
second_max = float('-inf')
for  i in arr:
    if i > max_val:
        second_max = max_val
        max_val = i
    elif i > second_max and i != max_val:
        second_max = i
    if i < min_val:
        min_val = i

print("Max:", max_val)
print("Second Largest:", second_max)
print("Min:", min_val)