class Solution:
    def maxProfit(self, prices: List[int])-> int:
        minn=99999
        maxprofit=0
        for x in range(len(prices)):
            if(prices[x]<minn):
                minn=prices[x]
            if(prices[x]-minn>maxprofit):
                maxprofit=prices[x]-minn
        return maxprofit
