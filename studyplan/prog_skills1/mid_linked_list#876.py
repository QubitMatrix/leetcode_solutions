# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        dhead=head
        while(dhead!=None):
            count+=1
            dhead=dhead.next
        mid=count//2+1
        count=0
        while(head!=None):
            count+=1
            if(count==mid):
                return head
            head=head.next
