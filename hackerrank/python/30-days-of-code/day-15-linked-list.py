class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        newNode = Node(data)
        if head is None:
            head = newNode
        else:
            current = head
            while(current.next is not None):
                current = current.next
            current.next = newNode
        return head
