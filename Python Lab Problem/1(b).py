from collections import deque 
class TollBoothQueue: 
    def __init__(self): 
        self.queue = deque() 
    # Insert vehicle into the queue 
    def insert(self, reg_no): 
        self.queue.append(reg_no) 
    # Remove (poll) vehicle from the queue 
    def poll(self): 
        if self.queue: 
            return self.queue.popleft() 
        else: 
            return None 
    # Display remaining vehicles 
    def display(self): 
        if self.queue: 
            print("Remaining Vehicles in Queue:", " ".join(self.queue)) 
        else: 
            print("No vehicles remaining in the queue.") 
# Input Section 
n = int(input("Enter number of vehicles: ")) 
vehicle_numbers = [] 
print("Enter the registration numbers:") 
for _ in range(n): 
    vehicle_numbers.append(input().strip()) 
x = int(input("Enter number of vechile(vehicles to pass): ")) 
# Initialize queue 
toll_queue = TollBoothQueue() 
# Insert vehicles into the queue 
for reg in vehicle_numbers: 
    toll_queue.insert(reg) 
# Poll vehicles (pass through toll) 
for _ in range(x): 
    toll_queue.poll() 
# Display remaining vehicles 
toll_queue.display()
