# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head=head
        dhead=head
        lenn=0
        while(dhead!=None):
            dhead=dhead.next
            lenn+=1
        self.len=lenn

    def getRandom(self) -> int:
        a=random.randrange(self.len)
        dhead=self.head
        count=0
        while(dhead!=None and count<a):
            dhead=dhead.next
            count+=1
        return dhead.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
