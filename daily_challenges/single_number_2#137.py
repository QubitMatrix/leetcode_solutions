from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic=defaultdict(int)
        for x in nums:
            dic[x]+=1
        return(list(filter(lambda x: dic[x]==1,dic.keys()))[0])
