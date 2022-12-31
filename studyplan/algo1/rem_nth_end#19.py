# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr=[]
        count=0
        dhead=head
        while(dhead!=None):
            count+=1
            arr.append(dhead)
            dhead=dhead.next
        pos=count-n
        if(count==1 and pos==0):
            return None
        elif(pos==0):
            return head.next
        else:
            t=arr[pos-1]
            try:
                t.next=arr[pos+1]
            except:
                t.next=None
            return head
