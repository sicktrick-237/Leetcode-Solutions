# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def printL(self, lst):
        while lst:
            print(lst.val)
            lst = lst.next

    def mergeList(self, l1, l2):
        prev = nxt = l1
        nxt = nxt.next
        while l2 and nxt:
            if nxt.val > l2.val:
                prev.next = ListNode(l2.val)
                prev.next.next = nxt
                prev = prev.next
                l2 = l2.next
                continue
            nxt = nxt.next
            prev = prev.next
            
        if not nxt:
            prev.next = l2
        return self.printL(l1)

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val < l2.val:
            return self.mergeList(l1, l2)
        else:
            return self.mergeList(l2, l1)

head = ListNode(20)
head.next = ListNode(50)
head.next.next = ListNode(70)
head.next.next.next = ListNode(90)
head.next.next.next.next = ListNode(100)


head2 = ListNode(10)
head2.next = ListNode(30)
head2.next.next = ListNode(40)
head2.next.next.next = ListNode(60)
head2.next.next.next = ListNode(120)


sol = Solution()
sol.mergeTwoLists(head, head2)