class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixsum={}
        s=0
        minlength=len(nums)
        for x in range(len(nums)):
            s+=nums[x]
            prefixsum[s]=x
        if(target>s):
            return 0
        for x in prefixsum.keys():
            if(x>=target):
                length=prefixsum[x]+1
                dif=x-target
                while(dif>0):
                    if(dif in prefixsum):
                        length=prefixsum[x]-prefixsum[dif]
                        break
                    else:
                        dif-=1
                minlength=min(minlength,length)
        return minlength
