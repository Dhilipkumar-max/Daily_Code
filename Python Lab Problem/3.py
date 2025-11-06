class StackNode: 
    def __init__(self, url): 
        self.url = url 
        self.next = None 

class StackHistory: 
    def __init__(self): 
        self.top = None 

    def push(self, url): 
        node = StackNode(url) 
        node.next = self.top 
        self.top = node 

    def pop(self): 
        if not self.top: 
            return None 
        url = self.top.url 
        self.top = self.top.next 
        return url 

class PrintJobNode: 
    def __init__(self, doc): 
        self.doc = doc 
        self.next = None 
class PrintQueue: 
    def __init__(self): 
        self.front = self.rear = None 
    def enqueue(self, doc): 
        node = PrintJobNode(doc) 
        if not self.rear:
            self.front = self.rear = node 
            return 
        self.rear.next = node 
        self.rear = node 
    def dequeue(self): 
        if not self.front: 
            return None 
        doc = self.front.doc 
        self.front = self.front.next 
        if not self.front: 
            self.rear = None 
        return doc 
history = StackHistory() 
history.push("google.com") 
history.push("openai.com") 
history.push("github.com") 
print("Last visited (popped):", history.pop()) 

print("Last visited (popped):", history.pop()) 
queue = PrintQueue() 

queue.enqueue("Document1.pdf") 
queue.enqueue("Document2.pdf") 
queue.enqueue("Document3.pdf") 

print("\nPrinting Jobs:") 
print("Printed:", queue.dequeue()) 
print("Printed:", queue.dequeue()) 
print("Printed:", queue.dequeue())
