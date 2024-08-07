# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        curr1 = head
        curr2 = head
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
        return curr1
            
            