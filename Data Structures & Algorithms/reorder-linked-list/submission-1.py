# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head2 = slow.next
        slow.next = None

        if not head2:
            return

        head2 = self.reverse(head2, None)

        # while head2:
        #     print(head2.val)
        #     head2 = head2.next
        
        head1 = head
        while head1 and head2:
            next1 = head1.next
            next2 = head2.next
            head1.next = head2
            head2.next = next1
            head2 = next2
            head1 = next1
        

    def reverse(self, current: Optional[ListNode], prev: Optional[ListNode]) -> ListNode:
        head = None
        if current.next:
            head = self.reverse(current.next, current)
        
        current.next = prev

        return head if head else current
        
