# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        binary = ""
        while curr != None:
            binary += str(curr.val)
            curr = curr.next
        return int(binary, 2)


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

sol = Solution()
sol.getDecimalValue(head)