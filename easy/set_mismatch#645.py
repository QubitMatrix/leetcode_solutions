class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=list(set([x for x in range(1,len(nums)+1)])-set(nums))
        nums.sort()
        for x in range(len(nums)-1):
            if(nums[x]==nums[x+1]):
                a.append(a[0])
                a[0]=nums[x]
                break
        return(a)
