class MinHeap: 
    def __init__(self): 
        self.heap = [] 
    def insert(self, patient_name, priority): 
        # Append the new patient 
        self.heap.append((priority, patient_name)) 
        self.__heapify_up(len(self.heap) - 1) 
    def extract_min(self): 
        if not self.heap: 
            print("No patients in queue.") 
            return None 
        if len(self.heap) == 1: 
            return self.heap.pop() 
        min_patient = self.heap[0] 
        self.heap[0] = self.heap.pop() 
        self.__heapify_down(0) 
        return min_patient 
    def __heapify_up(self, index): 
        parent = (index - 1) // 2 
        if index > 0 and self.heap[index][0] < self.heap[parent][0]: 
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index] 
            self.__heapify_up(parent) 
    def __heapify_down(self, index): 
        left = 2 * index + 1 
        right = 2 * index + 2 
        smallest = index 
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]: 
            smallest = left 
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]: 
            smallest = right 
        if smallest != index: 
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest] 
            self.__heapify_down(smallest) 
    def display(self): 
        print("Current ER Queue (Priority, Patient):") 
        for patient in self.heap: 
            print(f"Priority: {patient[0]} - Patient: {patient[1]}")  
        print() 
er_queue = MinHeap() 
er_queue.insert("Alice", 0)      
er_queue.insert("Bob", 3)        
er_queue.insert("Charlie", 1) 
er_queue.insert("David", 4) 
er_queue.insert("Eva", 2) 
er_queue.display()
print("Treating patients in order of severity:") 
while True: 
    patient = er_queue.extract_min() 
    if patient is None:
        break;
    print(f"Treating: {patient[1]} (Severity: {patient[0]})")
