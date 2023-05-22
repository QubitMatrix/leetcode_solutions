from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        for x in nums:
            dic[x]+=1
        dic=sorted(dic,key=lambda x:dic[x])
        return(dic[-1*k:])
