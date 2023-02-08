class Solution:
    def traverse(self,dic,src,des,memo):
        step=1
        minstep=9999999
        if(src==des):
            return 0
        if(src in memo):
            return memo[src]
        for x in dic[src]:
            step+=self.traverse(dic,x,des,memo) 
            minstep=min(minstep,step)
            step=1
        memo[src]=minstep
        return minstep       
            
    def jump(self, nums: List[int]) -> int:
        dic=defaultdict(list)
        for x in range(len(nums)):
            dic[x].extend(range(x+1,min(x+nums[x]+1,len(nums))))
        memo={}
        ans=self.traverse(dic,0,len(nums)-1,memo)
        return ans
