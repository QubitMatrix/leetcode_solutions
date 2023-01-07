class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        tank=0
        pos=0
        for x in range(len(gas)):
            tank+=gas[x]
            if(cost[x]>tank):
                tank=0
                pos=x+1
            else:
                tank-=cost[x]
        return pos
