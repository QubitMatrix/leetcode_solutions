class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic=defaultdict(int)
        dic[0]=1
        ans=0
        pre_sum=0
        for x in nums:
            pre_sum+=x
            rem=pre_sum%k
            ans+=dic[rem]
            dic[rem]+=1
        return ans
