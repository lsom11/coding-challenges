class MinStack(object):
    min=float('inf')
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min=float('inf')
        self.stack = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x<=self.min:
            self.stack.append(self.min)
            self.min = x
        self.stack.append(x)
    def pop(self):
        """
        :rtype: None
        """
        t = self.stack[-1]
        self.stack.pop()
        if self.min == t:
            self.min = self.stack[-1]
            self.stack.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()