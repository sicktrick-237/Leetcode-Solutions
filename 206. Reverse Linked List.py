class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head == None:
            return None
        string = []
        while head != None:
            string.append(head.val)
            head = head.next
        string = string[::-1]
        head = ListNode(string[0])
        curr = head
        for i in range(1,len(string)):
            curr.next = ListNode(string[i])
            curr = curr.next
        return head
    def reverseListAlternate(self, head):
        # Using Runner Technique - Two Pointers
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


head = ListNode(1)
first = ListNode(2)
second = ListNode(3)
third = ListNode(4)
fourth = ListNode(5)
head.next = first
first.next = second
second.next = third
third.next = fourth

sol = Solution()
sol.reverseList(head)