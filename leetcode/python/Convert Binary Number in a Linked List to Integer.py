class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        node = 0
        while (temp):
            node += 1
            temp = temp.next
        result = 0
        for i in range(node):
            result += head.val * 2 ** (node - 1 - i)
            head = head.next
        return result