# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dhead=head
        count=0
        while(dhead!=None):
            count+=1
            if(count==k):
                val1=dhead
            dhead=dhead.next
            
        pos=0
        dhead=head
        while(pos!=(count-k)):
            pos+=1
            dhead=dhead.next
            
        val2=dhead
        val1.val,val2.val=val2.val,val1.val
        return head
