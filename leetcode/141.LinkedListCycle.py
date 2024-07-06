# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        curr1, curr2 = head, head
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
            if curr1 == curr2:
                return True
        return False
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        curr = head
        seen = set()
        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next
        return False