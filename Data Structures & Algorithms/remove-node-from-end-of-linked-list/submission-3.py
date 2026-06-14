# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        prev = None
        count = 0
        index = 0

        while curr:
            curr = curr.next
            count += 1
        
        if count == 1:
            return None
        
        if count == 2 and n == 1:
            head.next = None
            return head
        elif count-n == 0:
            return head.next

        curr = head

        while curr:
            if index == count - n:
                nxt = curr.next
                prev.next = nxt
                return head
            else:
                prev = curr
                curr = curr.next
                index += 1
