# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dhead=head
        prev=None
        while(head!=None):
            if(head.val==val):
                if(prev==None):
                    head=head.next
                    dhead=head
                else:
                    prev.next=head.next
                    head=head.next
            else:
                prev=head
                head=head.next
        return dhead
