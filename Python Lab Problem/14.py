def quick_sort(items): 
    if len(items) <= 1: 
        return items 
    else: 
        pivot = items[len(items) // 2] 
        left = [x for x in items if x < pivot] 
        middle = [x for x in items if x == pivot]  
        right = [x for x in items if x > pivot]
        return quick_sort(left) + middle + quick_sort(right) 
item_sizes = [45, 12, 78, 23, 56, 10, 89, 33] 
print("Original Item Sizes (in cm):") 
print(item_sizes) 
sorted_sizes = quick_sort(item_sizes) 
print("\nSorted Item Sizes (in cm):") 
print(sorted_sizes)