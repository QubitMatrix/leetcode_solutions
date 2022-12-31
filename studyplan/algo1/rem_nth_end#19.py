# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        dhead=head
        while(dhead!=None):
            count+=1
            dhead=dhead.next
        pos=count-n
        if(pos==0 and count==1):
            return None
        prev=None
        dhead=head
        count=0
        while(count<pos):
            prev=dhead
            dhead=dhead.next
            count+=1
        if(not prev):
            head=head.next
        else:
            prev.next=dhead.next
        return head
