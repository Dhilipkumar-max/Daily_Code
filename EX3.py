def binary_search(arr, target):
    low, high = 1, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        if arr[mid] < target: low = mid
        else: high = mid
    return -1
