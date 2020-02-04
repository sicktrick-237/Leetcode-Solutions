class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        curr = head
        temp = ListNode(curr.val)
        tempcurr = temp
        while curr != None and curr.next != None:
            if curr.val != curr.next.val:
                tempcurr.next = ListNode(curr.next.val)
                tempcurr = tempcurr.next
            curr = curr.next
        return temp
        


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
sol = Solution()
sol.deleteDuplicates(head)