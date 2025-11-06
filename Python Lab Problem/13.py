def merge_sort(expenses): 
    if len(expenses) > 1: 
        mid = len(expenses) // 2 
        left_half = expenses[:mid] 
        right_half = expenses[mid:] 
        merge_sort(left_half) 
        merge_sort(right_half) 
        i = j = k = 0 
        while i < len(left_half) and j < len(right_half): 
            if left_half[i][1] < right_half[j][1]: 
                expenses[k] = left_half[i] 
                i += 1 
            else: 
                expenses[k] = right_half[j] 
                j += 1 
            k += 1 
        while i < len(left_half): 
            expenses[k] = left_half[i] 
            i += 1 
            k += 1 
        while j < len(right_half): 
            expenses[k] = right_half[j] 
            j += 1 
            k += 1 
monthly_expenses = [ 
    ("Rent", 15000), 
    ("Food", 5000), 
    ("Utilities", 3000), 
    ("Travel", 4500), 
    ("Miscellaneous", 2500) 
] 
print("Original Monthly Expenses:") 
for category, amount in monthly_expenses: 
    print(f"{category}: ₹{amount}") 

merge_sort(monthly_expenses) 
print("\nSorted Monthly Expenses (Ascending):") 
for category, amount in monthly_expenses: 
 print(f"{category}: ₹{amount}")