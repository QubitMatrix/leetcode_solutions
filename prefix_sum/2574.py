class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum=[]
        rightsum=[]
        prev=0
        total=sum(nums)
        
        for x in nums:
            cur=prev+x
            leftsum.append(prev)
            rightsum.append(total-cur)
            prev=cur
        ans=[]
        
        for x in range(len(nums)):
            ans.append(int(math.fabs(leftsum[x]-rightsum[x])))
        return ans
        
