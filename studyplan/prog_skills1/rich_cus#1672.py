class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum1=[sum(x) for x in accounts ]
        return max(sum1)
