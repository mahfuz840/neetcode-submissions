# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None
        
        head = None
        if list1.val < list2.val:
            print('list1 ', list1.val)
            head = list1
            list1 = list1.next
        else:
            print('list2 ', list2.val)
            head = list2
            list2 = list2.next
        
        ans = head
        
        while list1 and list2:
            if list1.val < list2.val:
                print('list1 ', list1.val)
                head.next = list1
                list1 = list1.next
            else:
                print('list2 ', list2.val)
                head.next = list2
                list2 = list2.next
            
            head = head.next
        
        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next
        
        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next
        
        return ans
