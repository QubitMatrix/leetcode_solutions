class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m=99999
        n=0
        for x in nums:
            m=min(m,x)
            n=max(n,x)
        for x in range(m,1,-1):
            if(n%x==0 and m%x==0):
                return x
        return 1
