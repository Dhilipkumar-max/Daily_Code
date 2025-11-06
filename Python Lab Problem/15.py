class HashTable: 
    def __init__(self, size): 
        self.size = size 
        self.table_linear = [None for _ in range(size)] 
        self.table_quadratic = [None for _ in range(size)] 
 
    def linear_probing_insert(self, key): 
        index = key % self.size 
        start_index = index  # Save for cycle check 
        while self.table_linear[index] is not None: 
            index = (index + 1) % self.size 
            if index == start_index: 
                print("Hash Table is Full - Linear Probing") 
                return 
        self.table_linear[index] = key 
    def quadratic_probing_insert(self, key): 
        index = key % self.size 
        i = 1 
        start_index = index 
        while self.table_quadratic[index] is not None: 
            index = (start_index + i ** 2) % self.size 
            i += 1 
            if i == self.size: 
                print("Hash Table is Full - Quadratic Probing") 
                return 
        self.table_quadratic[index] = key 
    def display(self): 
        print("\nHash Table (Linear Probing):") 
        for i, val in enumerate(self.table_linear): 
            print(f"Index {i}: {val}") 
        print("\nHash Table (Quadratic Probing):") 
        for i, val in enumerate(self.table_quadratic): 
            print(f"Index {i}: {val}") 
 
 
hash_table = HashTable(7) 
keys_linear = [10, 20, 5, 15, 7] 
for key in keys_linear: 
    hash_table.linear_probing_insert(key) 
keys_quadratic = [10, 20, 5, 15, 7] 
for key in keys_quadratic: 
    hash_table.quadratic_probing_insert(key) 
hash_table.display() 