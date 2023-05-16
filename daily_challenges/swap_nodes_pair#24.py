# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead=head
        prev=None
        count=0
        while(dhead!=None):
            if(not dhead.next):
                break
            temp=dhead.next.next
            if(prev):
                prev.next=dhead.next
            else:
                head=dhead.next
            dhead.next.next=dhead
            dhead.next=temp
            prev=dhead
            dhead=dhead.next
        return(head)
