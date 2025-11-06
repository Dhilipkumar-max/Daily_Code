inventory = [ 
    {"id": 101, "name": "Laptop"}, 
    {"id": 202, "name": "Smartphone"}, 
    {"id": 303, "name": "Tablet"}, 
    {"id": 404, "name": "Headphones"} 
] 
def linear_search(inventory, product_id): 
    for idx, product in enumerate(inventory): 
        if product['id'] == product_id: 
            return idx, product 
 
    return -1, None 
def binary_search(inventory, product_id): 
    left, right = 0, len(inventory) - 1 
    while left <= right: 
        mid = (left + right) // 2 
        if inventory[mid]['id'] == product_id: 
            return mid, inventory[mid] 
        elif inventory[mid]['id'] < product_id: 
            left = mid + 1 
        else: 
            right = mid - 1 
    return -1, None 
print("Linear Search Result:") 
idx, product = linear_search(inventory, 303) 
if idx != -1: 
    print(f"Product found at index {idx}: {product}") 
else: 
    print("Product not found.") 
sorted_inventory = sorted(inventory, key=lambda x: x['id']) 
print("\nBinary Search Result:") 
idx, product = binary_search(sorted_inventory, 404) 
if idx != -1: 
    print(f"Product found at index {idx}: {product}") 
else: 
    print("Product not found.")