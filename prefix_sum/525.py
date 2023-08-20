class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlength=0
        s=0
        dic={}
        for x in range(len(nums)):
            s+=1 if nums[x]==1 else -1
            length=0
            if s==0:
                length=x+1
            elif s in dic:
                length=x-dic[s]
            else:
                dic[s]=x
            maxlength=max(maxlength,length)
        return maxlength
            
