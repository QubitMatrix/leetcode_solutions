class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(nums==[]):
            return []
        start=nums[0]
        arr=[]
        for x in range(len(nums)-1):
            if(nums[x]+1!=nums[x+1]):
                if(start==nums[x]):
                    arr.append(str(start))
                else:
                    arr.append(str(start)+"->"+str(nums[x]))
                start=nums[x+1]
        if(start==nums[-1]):
            arr.append(str(start))
        else:
            arr.append(str(start)+"->"+str(nums[-1]))
        return arr
