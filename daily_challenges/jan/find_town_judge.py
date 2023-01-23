class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s=set(range(1,n+1))
        is_trusted=defaultdict(int)
        trusts=defaultdict(int)
        if(n==1 and trust==[]):
            return 1
        for x,y in trust:
            is_trusted[y]+=1
            trusts[x]+=1
        l=sorted(is_trusted.items(),key=lambda x:x[1])
        for x in l:
            if(x[1]==n-1 and trusts[x[0]]==0):
                return x[0]
        return -1
