# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        while(head!=None and id(head) not in s):
            s.add(id(head))
            head=head.next
        if(id(head) in s):
            return True
        else:
            return False
