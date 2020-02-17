# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        curr = prev = head
        while curr:
            if curr.val == val and curr == head:
                head = head.next
                curr = prev = head
                continue
            if curr.next and curr.next.val == val:
                prev.next = curr.next.next
                if curr.next and curr.next.val == val:
                    continue
            curr = curr.next
            prev = prev.next
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

val = 2

sol = Solution()
sol.removeElements(head, val)