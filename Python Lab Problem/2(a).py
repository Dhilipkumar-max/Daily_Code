class Node: 
    def __init__(self, name, number): 
        self.name = name 
        self.number = number 
        self.next = None 
class ContactList: 
    def __init__(self): 
        self.head = None 
    def insert_at_end(self, name, number): 
        new_node = Node(name, number) 
        if not self.head: 
            self.head = new_node 
            return 
        last = self.head 
        while last.next: 
            last = last.next 
        last.next = new_node 
    def delete_contact(self, name): 
        temp = self.head 
        prev = None 
        while temp and temp.name != name: 
            prev = temp 
            temp = temp.next 
        if not temp: 
            print("Contact not found") 
            return 
        if prev: 
            prev.next = temp.next 
        else: 
            self.head = temp.next 
    def display(self): 
        temp = self.head 
        while temp: 
            print(f"{temp.name}: {temp.number}") 
            temp = temp.next 
contacts = ContactList()
contacts.insert_at_end("Alice", "12345") 
contacts.insert_at_end("Bob", "67890") 
contacts.insert_at_end("Charlie", "54321") 
print("Contact List after insertion:") 
contacts.display() 
print("\nDeleting Bob...") 
contacts.delete_contact("Bob") 
print("\nContact List after deletion:") 
contacts.display() 
print("\nDeleting Eve (not in list)...") 
contacts.delete_contact("Eve") 
print("\nFinal Contact List:") 
contacts.display() 
