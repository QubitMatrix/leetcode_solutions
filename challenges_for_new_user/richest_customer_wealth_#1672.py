class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row=len(accounts)
        col=len(accounts[0])
        max1=0
        sum_f=0
        for x in accounts:
            sum_f=0
            for y in x:
                sum_f+=y
            if(sum_f>max1):
                max1=sum_f
        return max1
