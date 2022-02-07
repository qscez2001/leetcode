'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
'''

# not O(1) time solved
class MinStack:
    from collections import deque
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = deque()

    def push(self, x: int) -> None:
        self.d.append(x)

    def pop(self) -> None:
        self.d.pop()

    def top(self) -> int:
        return self.d[-1]
        
    def getMin(self) -> int:
        return min(self.d)

# Approach 1: Stack of Value/ Minimum Pairs
'''
An invariant is something that is always true or consistent. You should always be on the lookout for useful invariants when problem-solving in math and computer science.

Recall that with a Stack, we only ever add (push) and remove (pop) numbers from the top. Therefore, an important invariant of a Stack is that when a new number, which we'll call x, is placed on a Stack, the numbers below it will not change for as long as number x remains on the Stack. Numbers could come and go above x for the duration of x's presence, but never below.

So, whenever number x is the top of the Stack, the minimum will always be the same, as it's simply the minimum out of x and all the numbers below it.
'''

class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
        
        
    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
