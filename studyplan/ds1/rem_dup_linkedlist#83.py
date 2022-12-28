# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dhead=head
        prev=None
        while(head!=None):
            
            if(prev!=None):
                if(prev.val==head.val):
                    prev.next=head.next
                else:
                    prev=head
                head=head.next
            else:
                prev=head
                head=head.next
        return dhead
