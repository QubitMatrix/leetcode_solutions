class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s=0
        dic={0:0}
        for x in range(len(nums)):
            s+=nums[x]
            rem=s%k
            if rem not in dic:
                dic[rem]=x+1
            elif dic[rem]<x:
                return True
        return False
