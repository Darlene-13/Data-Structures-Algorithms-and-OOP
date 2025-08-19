"""
This is a file for the stack data structure.

It contains the implementation of a stack using a list.
It includes all its basic operations like push, pop, peek, and is_empty.
Key operation is to always check if the stack is empty first before popping or peeking.
"""


# Stack is a data structure that basically follows the LIFO structure of first in last out.


"""
Common use cases:

- Undo functionality in text editors
- Call stack in programming languages execution.
- Backtracking algorithms (like maze solving).
- Parsing expressions in compilers.
- Implementing function calls and returns.


"""
class Stack:
    def __init__(self):
        # Initialize and empty stack.
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self._is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        if self._is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    

    def size(self):
        return len(self.items)
    


# Real world example:
"""
Check if the paranthesis of a string is balanced or not.
"""
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()