class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix_sum={}
        prefix_sum[0]=1
        for x in range(1,n):
            prefix_sum[x]=prefix_sum[x-1]+x+1
        if(prefix_sum[n-1]-prefix_sum[0]==0):
            return 1
        for x in range(2,n+1):
            if(prefix_sum[x-2]==prefix_sum[n-1]-prefix_sum[x-1]):
                return x
        return -1
