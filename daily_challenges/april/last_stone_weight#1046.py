class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            stones.sort()
            x=stones.pop()
            y=stones.pop()
            if(x!=y):
                stones.append(int(math.fabs(x-y)))
        return stones[0] if len(stones)==1 else 0
