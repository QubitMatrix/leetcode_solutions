class Solution:
    def partition(self, s: str) -> List[List[str]]:
        arr=[]
        def palin(st):
            return st==st[::-1]
        def backtrack(pos,cur):
            #print(pos,cur)
            if(pos==len(s)):
                arr.append(cur)
            for x in range(pos,len(s)):
                t=s[pos:x+1]
                if(palin(t)):
                    backtrack(x+1,cur+[t])
                    #print(pos,cur)
        backtrack(0,[])
        return arr
