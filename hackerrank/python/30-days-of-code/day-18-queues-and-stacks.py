class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []

    # push to END
    def pushCharacter(self, char):
        self.stack.append(char)

    # insert at BEGINNING
    def enqueueCharacter(self, char):
        self.queue.insert(0, char)

    # pop at BEGINNING
    def popCharacter(self):
        return self.stack.pop()

    # pop at BEGINNING
    def dequeueCharacter(self):
        return self.queue.pop()
