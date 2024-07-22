# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        arr = arr[::-1]
        res = 0
        n = len(arr) 
        i = 0
        while i < n:
            mul = 2 ** i
            ans = arr[i] * mul
            res += ans
            i += 1
        return res
        
