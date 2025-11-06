def reverse_book_ids(): 
    stack = [] 
    num_books = int(input("Enter the number of books: ")) 
 
    print("Enter the book IDs:") 
    for _ in range(num_books): 
        book_id = input() 
        stack.append(book_id) 
 
    print("\nBook IDs in reverse order:") 
    while stack: 
        print(stack.pop()) 
if __name__ == "__main__": 
    reverse_book_ids()
