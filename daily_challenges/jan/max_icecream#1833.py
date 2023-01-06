class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        for x in costs:
            if(x<=coins):
                coins-=x
                count+=1
            else:
                break
        return count
