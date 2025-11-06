def heapify(arr, n, i): 
    largest = i 
 
    left = 2 * i 
    right = 2 * i + 1 
    if left <= n and arr[left] > arr[largest]: 
        largest = left  
    if right <= n and arr[right] > arr[largest]: 
        largest = right 

    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i] 
        heapify(arr, n, largest) 
def buildMaxHeap(arr, n): 
    for i in range(n // 2, 0, -1): 
        heapify(arr, n, i) 
 
def heapSort(arr, n): 
    buildMaxHeap(arr, n) 
    for i in range(n, 1, -1): 
        arr[1], arr[i] = arr[i], arr[1] 
        heapify(arr, i - 1, 1)
arr = [None] + [20, 5, 15, 22, 40, 10] 
n = len(arr) - 1 
print("Original Array (1-based indexing):") 
print(arr[1:])
heapSort(arr, n)
print("\nElements in Descending Order after Heap Sort:") 
print(arr[1:])