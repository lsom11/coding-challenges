class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return not len(self.stack)

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()
