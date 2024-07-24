# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def helper_recursive(self, prev, current):
        if current.next is None:
            current.next = prev
            return current

        temp = current.next
        current.next = prev
        prev = current
        current = temp
        return self.helper_recursive(prev, current)
    def reverseList(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        current = head
        next_curr = current.next
        current.next = None
        new_head = self.helper_recursive(current, next_curr)
        return new_head