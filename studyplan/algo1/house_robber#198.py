class Solution:
    
        
    def rob(self, nums: List[int]) -> int:
        self.mem=[-1 for x in range(100)]
        return self.robb(nums,len(nums)-1)
    def robb(self,nums,i):
        if(i<0):
            return 0
        elif(self.mem[i]>=0):
            return self.mem[i]
        else:
            res=max(self.robb(nums,i-2)+nums[i],self.robb(nums,i-1))
            self.mem[i]=res
            return res
