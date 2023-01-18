class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        l=len(nums)
        right_max=[0 for x in range(l)]
        right_max[l-1]=nums[l-1]
        suffix_max=nums[l-1]
        for x in range(l-2,-1,-1):
            suffix_max+=nums[x]
            right_max[x]=max(right_max[x+1],suffix_max)
        prefix_sum=0
        cir_sum=nums[0]
        for x in range(0,l-1):
            prefix_sum+=nums[x]
            cir_sum=max(cir_sum,prefix_sum+right_max[x+1])
        cur_max=nums[0]
        lin_max=nums[0]
        for x in range(1,l):
            cur_max=max(nums[x],cur_max+nums[x])
            lin_max=max(lin_max,cur_max)
        return max(lin_max,cir_sum)
