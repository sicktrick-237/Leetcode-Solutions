class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        first = head
        init = []
        if not head or not head.next:
            return head
        
        while first != None:
            init.append(first.val)
            first = first.next
        k = k % len(init)
        
        while k > 0:
            init = [init[-1]] + init[:-1]
            k -= 1
            

        head = ListNode(init[0])
        curr = head
        i = 1
        while i <= len(init[1:]):
            curr.next = ListNode(init[i])
            curr = curr.next
            i += 1
        return head


head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)

sol = Solution()
k = 4
sol.rotateRight(head, k)