def find_target(arr, t):
    for i in range(len(arr)):
        if t == arr[i]:
            print(f"Target found at indx :{i}")
            return
    print("Not found")

arr = [2, 5, 7, 89, 3, 2]
target = int(input("Enter the taget to be find:"))
find_target(arr, target)
