class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        l1=nums[0:n]
        l2=nums[n:]
        for x in range(0,n,1):
            l.extend((l1[x],l2[x]))
        return l
