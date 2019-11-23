class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
      return len(self.queue)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return not len(self.queue)

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        return self.queue.pop(0)
