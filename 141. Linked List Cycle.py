# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
     def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        if not head:
            return
        nodemap = {}
        while curr:
            if curr not in nodemap:
                nodemap[curr] = 1
                curr = curr.next
                continue
            return True
        return False



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = head.next
sol = Solution()
sol.hasCycle(head)