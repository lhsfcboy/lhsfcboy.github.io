
"""
Implement a stack with min() function, which will return the smallest number in the stack.

It should support push, pop and min operation all in O(1) cost.
"""



class MinStack:
    
    def __init__(self):
        self.main_stack = []
        self.min_number = []
        
    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        self.main_stack.append(number)
        if len(self.min_number) == 0 or number <= self.min_number[-1]:
            self.min_number.append(number)
        # write your code here

    """
    @return: An integer
    """
    def pop(self):
        top = self.main_stack[-1]
        self.main_stack.pop()
        if top == self.min_number[-1]:
            self.min_number.pop()
        # write your code here
        return top
    """
    @return: An integer
    """
    def min(self):
        return self.min_number[-1]
        # write your code here
