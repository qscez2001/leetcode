def isValid(s: str):
    stack = []
    # if len(s) % 2 == 1:
    #     return False
    for c in s:
        if c == '(' or c == '{' or c == '[':
            stack.append(c)
        else:
            if not stack:
                return False
            if c == ')':
                a = stack.pop()
                if a != '(':
                    return False
            elif c == ']':
                a = stack.pop()
                if a != '[':
                    return False
            elif c == '}':
                a = stack.pop()
                if a != '{':
                    return False
    # print(stack)
    if stack:
        return False

    return True

def isValid(self, s: str) -> bool:
    stack = []
    
    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}
    
    for c in s:
        
        # If the character is an closing bracket
        if c in mapping:
            if stack:
                top = stack.pop()
            else:
                top = "#"
            
            if mapping[c] != top:
                return False
        
        else:
            stack.append(c)
            
    if stack:
        return False

    return True

s = "()"
print(isValid(s))