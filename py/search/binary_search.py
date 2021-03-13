

def binarySearch(arr, target):
    arr.sort()
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    list1 = [1,2,3,4,5,6,7,8,9]
    target = 3
    index = binarySearch(list1, target)
    print("Target {} was found at position {}".format(target, index))