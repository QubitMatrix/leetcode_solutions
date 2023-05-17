# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        dhead=head
        arr=[]
        sum1=0
        while(dhead!=None):
            arr.append(dhead.val)
            dhead=dhead.next
        for x in range(len(arr)//2):
            sum1=max(arr[x]+arr[-1*(x+1)],sum1)
        return sum1
