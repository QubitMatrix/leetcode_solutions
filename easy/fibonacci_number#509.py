class Solution:
    def fib(self, n: int) -> int:
        mem={}
        mem[0]=0
        mem[1]=1
        x=2
        while(x<=n):
            mem[x]=mem[x-1]+mem[x-2]
            x+=1
        return mem[n]

a=Solution()
print(a.fib(3))
