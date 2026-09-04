# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        lastNode = None

        while head:
            nextNode = head.next
            head.next = lastNode
            lastNode = head
            head = nextNode
        
        return lastNode
