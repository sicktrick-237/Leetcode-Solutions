# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        if not head:
            return
        nodemap = []
        while curr:
            nodemap.append(curr.val)
            curr = curr.next
        nodemap.sort()
        new = ListNode(nodemap[0])
        curr = new
        for each in range(1,len(nodemap)):
            curr.next = ListNode(nodemap[each])
            curr = curr.next
        return new




head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(4)
head.next.next.next = ListNode(3)
sol = Solution()
sol.sortList(head)