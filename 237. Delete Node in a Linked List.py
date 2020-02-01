# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printList(self, node):
        while node != None:
            print(node.val)
            node = node.next
    def deleteNode(self, head, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # curr = head
        #prev = curr
        if node.next != None:
            node.val = node.next.val # Assign Current
            node.next = node.next.next
            self.printList(head)
        


head = ListNode(4)
head.next = ListNode(5)
# head.next.next = ListNode(1)
# head.next.next.next = ListNode(9)
sol = Solution()
sol.deleteNode(head, head)
