class PolyNode: 
    def __init__(self, coeff, exp): 
        self.coeff = coeff 
        self.exp = exp 
        self.next = None 
class Polynomial: 
    def __init__(self): 
        self.head = None 
    def insert_term(self, coeff, exp): 
        new_node = PolyNode(coeff, exp) 
        if (self.head is None) or (self.head.exp < exp): 
            new_node.next = self.head 
            self.head = new_node 
        else: 
            current = self.head 
            while current.next and current.next.exp > exp: 
                current = current.next 
            if current.next and current.next.exp == exp: 
                current.next.coeff += coeff 
            else: 
                new_node.next = current.next 
                current.next = new_node 
    def display(self): 
        terms = [] 
        current = self.head 
        while current: 
            if current.exp == 0: 
                terms.append(f"{current.coeff}") 
            elif current.exp == 1: 
                terms.append(f"{current.coeff}x") 
            else: 
                terms.append(f"{current.coeff}x^{current.exp}") 
            current = current.next 
        print(" + ".join(terms) if terms else "0") 
    @staticmethod 
    def add(poly1, poly2): 
        result = Polynomial() 
        p1 = poly1.head 
        p2 = poly2.head 
        while p1 and p2: 
            if p1.exp > p2.exp: 
                result.insert_term(p1.coeff, p1.exp) 
                p1 = p1.next 
            elif p1.exp < p2.exp: 
                result.insert_term(p2.coeff, p2.exp) 
                p2 = p2.next 
            else: 
                result.insert_term(p1.coeff + p2.coeff, p1.exp) 
                p1 = p1.next 
                p2 = p2.next 
        while p1: 
            result.insert_term(p1.coeff, p1.exp) 
            p1 = p1.next 
        while p2: 
            result.insert_term(p2.coeff, p2.exp) 
            p2 = p2.next 
        return result 
    def evaluate(self, x): 
        result = 0 
        current = self.head 
        while current: 
            result += current.coeff * (x ** current.exp) 
            current = current.next 
        return result 
tax1 = Polynomial() 
tax1.insert_term(3, 2) 
tax1.insert_term(2, 1) 
tax1.insert_term(5, 0) 
tax2 = Polynomial() 
tax2.insert_term(2, 2) 
tax2.insert_term(4, 0) 
print("Tax Formula 1:") 

tax1.display() 
print("Tax Formula 2:") 
tax2.display() 
combined_tax = Polynomial.add(tax1, tax2) 
print("Combined Tax Formula:") 
combined_tax.display() 

result = combined_tax.evaluate(2) 
print(f"Tax Amount for income=2: {result}")
