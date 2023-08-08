class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prev_sum=0
        minval=0
        for x in nums:
            cur_sum=prev_sum+x
            prev_sum=cur_sum
            if(cur_sum<0 and cur_sum<minval):
                minval=cur_sum
        return minval*-1+1 if minval else 1
