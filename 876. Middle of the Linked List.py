class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def makeList(self, list):
        curr = ListNode(list[0])
        head = curr
        for i in range(1, len(list)):
            head.next = ListNode(list[i])
            head = head.next
        return curr

    def middleNode(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        elements = []
        while curr != None:
            elements.append(curr.val)
            curr = curr.next
        count = len(elements)
        # if count % 2 == 0 and count > 2:
        #     return self.makeList(elements[count//2:])
        return self.makeList(elements[count//2:])



head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
sol = Solution()
sol.middleNode(head)