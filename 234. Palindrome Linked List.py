# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        original = ""
        reverse = ""
        while curr:
            original += str(curr.val)
            reverse = str(curr.val) + reverse
            curr = curr.next
        return True if original == reverse else False
        
        


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

sol = Solution()
sol.isPalindrome(head)