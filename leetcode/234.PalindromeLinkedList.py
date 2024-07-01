# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        def isPalindromeHelper(right):
            nonlocal left

            if right is None:
                return True

            if not isPalindromeHelper(right.next):
                return False
            
            if right.val != left.val:
                return False

            left = left.next

            return True
        left = head
        return isPalindromeHelper(head)