def isValid(s: str):
    stack = []
    if len(s) % 2 == 1:
        return False
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


s = "()"
print(isValid(s))