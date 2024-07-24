# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def helper_rec(self, current, val):
        if current is None or current.next is None:
            return
        if current.next.val == val:
            next_curr = current.next
            while next_curr is not None and next_curr.val == val:
                next_curr = next_curr.next
            current.next = next_curr

        self.helper_rec(current.next, val)

    def removeElements(self, head, val):
        if head is None:
            return None
        dummy = ListNode(0)
        dummy.next = head 

        self.helper_rec(dummy, val)
        return dummy.next
        
        