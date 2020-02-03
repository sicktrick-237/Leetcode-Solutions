"""
Given a linked list, swap every two adjacent nodes
and return its head.
For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.
Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""

class ListNode(object):
    def __init__(self, data):
        self.val = data
        self.next = None

class Solution:
    def printList(self, head):
        while head!=None:
            print(head.val)
            head = head.next

    def swapList(self, head):
        curr = head
        if head:
            while curr != None and curr.next != None:
                curr.val, curr.next.val = curr.next.val, curr.val
                curr = curr.next.next
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution()
sol.swapList(head)