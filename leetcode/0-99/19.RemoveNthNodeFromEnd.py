class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None or head.next is None:
            return None
        length = self.findLength(head)
        target = length - n 
        curr = head
        prev = None
        counter = 0
        while curr is not None:
            if counter == target:
                if not prev:
                    head = curr.next
                else:
                    prev.next = curr.next
                break
            counter += 1
            prev = curr
            curr = curr.next
        return head

    def findLength(self, head):
        l = 0
        curr = head
        while curr is not None:
            l += 1
            curr = curr.next
        return l

# Second Approach:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        curr = dummy

        for i in range(n):
            head = head.next

        while head:
            head = head.next
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next