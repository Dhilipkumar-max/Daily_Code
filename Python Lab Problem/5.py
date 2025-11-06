def infix_to_postfix(expression): 
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3} 
    stack = [] 
    result = '' 
    for char in expression: 
        if char.isalnum(): 
            result += char 
        elif char == '(': 
            stack.append(char) 
        elif char == ')': 
            while stack and stack[-1] != '(': 
                result += stack.pop() 
            stack.pop() 
        else: 
            while stack and stack[-1] != '(' and precedence.get(stack[-1],0) >= precedence[char]: 
                result += stack.pop() 
            stack.append(char) 
    while stack: 
        result += stack.pop() 
    return result 
def evaluate_postfix(expression): 
    stack = [] 
    for char in expression: 
        if char.isdigit(): 
            stack.append(int(char)) 
        else: 
            b = stack.pop() 
            a = stack.pop() 
            if char == '+': 
                stack.append(a + b) 
            elif char == '-': 
                stack.append(a - b) 
            elif char == '*': 
                stack.append(a * b) 
            elif char == '/': 
                stack.append(a // b) 
    return stack.pop() 
expression = "(3+5)*2" 
postfix = infix_to_postfix(expression) 
result = evaluate_postfix(postfix) 
print("Infix Expression:", expression) 
print("Postfix Expression:", postfix) 
print("Evaluated Result:", result)
