array = [1,2,3,4,5,6,7]
target = 6
low, high = 0, len(array) - 1

while low<=high:
    mid = (low + high) // 2
    pos = array[mid]
    print(mid)

    if pos == target:
        print("Target is found and it is: ", pos)
        break
    elif pos < target:
        print("Target is probably to the right")
        low = mid + 1
    elif pos > target:
        print("Target is probably to the left")
        high = mid - 1
    else: 
        print("man")
