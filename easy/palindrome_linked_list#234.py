# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        while(head!=None):
            arr.append(head.val)
            head=head.next
        for x in range(len(arr)//2):
            if(arr[x]!=arr[-1*(x+1)]):
                return False
        return True
