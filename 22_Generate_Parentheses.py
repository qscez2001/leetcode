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

# Memory limit exceed
def generateParenthesis(n):
    from itertools import permutations 
    string = n*'(' + n*')'
    # print(string)
    list1 = list(permutations(string))
    # new = []
    # for l in list1:
    #     new.append(list(l))
    # print(new)
    ans = []
    for item in list1:
        str1 = "".join(item)
        ans.append(str1)
    # print(len(ans))

    new = []
    for a in ans:
        if isValid(a) and a not in new:
            new.append(a)


    return new

# others solution
def generateParenthesis(n):
    def generate(A = []):
        if len(A) == 2*n:
            if valid(A):
                ans.append("".join(A))
        else:
            A.append('(')
            generate(A)
            A.pop()
            A.append(')')
            generate(A)
            A.pop()

    def valid(A):
        bal = 0
        for c in A:
            if c == '(': bal += 1
            else: bal -= 1
            if bal < 0: return False
        return bal == 0

    ans = []
    generate()
    return ans





n = 3
print(generateParenthesis(3))



'''
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''