class Stack: 
    def __init__(self, max_size): 
        self.items = [] 
        self.max_size = max_size 
    def push(self, item): 
        if len(self.items) == self.max_size: 
            print("Stack Overflow") 
        else: 
            self.items.append(item) 
    def pop(self): 
        if not self.items: 
            print("Stack Underflow") 
        else: 
            return self.items.pop()  
class Queue: 
    def __init__(self, max_size): 
        self.queue = [] 
        self.max_size = max_size 
    def enqueue(self, item): 
        if len(self.queue) == self.max_size: 
            print("Queue is Full") 
        else: 
            self.queue.append(item) 
    def dequeue(self): 
        if not self.queue: 
            print("Queue is Empty") 
        else: 
            return self.queue.pop(0) 
# Circular Queue Implementation 
class CircularQueue: 
    def __init__(self, size): 
        self.size = size 
        self.queue = [None] * size 
        self.front = self.rear = -1 
    def enqueue(self, item): 
        if (self.rear + 1) % self.size == self.front: 
            print("Circular Queue is Full") 
        elif self.front == -1: 
            self.front = self.rear = 0 
            self.queue[self.rear] = item 
        else: 
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = item 
 
    def dequeue(self): 
        if self.front == -1: 
            print("Circular Queue is Empty") 
        elif self.front == self.rear: 
            temp = self.queue[self.front] 
            self.front = self.rear = -1 
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 
print("=== Stack Test ===") 
stack = Stack(5) 
stack.push('KA01AB1234') 
stack.push('KA01CD5678') 
print("Popped:", stack.pop())  # Expected 'KA01CD5678' 
# Queue test 
print("\n=== Queue Test ===") 
queue = Queue(5) 
queue.enqueue('KA41EF4321') 
print("Dequeued:", queue.dequeue())  # Expected 'KA41EF4321' 
 
# Circular Queue test 
print("\n=== Circular Queue Test ===") 
cq = CircularQueue(5) 
cq.enqueue('KA17HG7070') 
cq.enqueue('KA15DE9981') 
print("Dequeued:", cq.dequeue())  # Expected 'KA17HG7070'
