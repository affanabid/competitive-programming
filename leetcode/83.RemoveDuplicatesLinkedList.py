# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head):
        curr = head
        prev = None
        seen = set()
        while curr:
            if curr.val in seen:
                temp = curr
                while temp and temp.val == curr.val:
                    temp = temp.next
                prev.next = temp
            else:
                seen.add(curr.val) 
            prev = curr
            curr = curr.next
        return head
    def disp(self, head):
        while head:
            print(head.val)
            head = head.next
        print()

l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)

s = Solution()
s.disp(l)
s.deleteDuplicates(l)
s.disp(l)
