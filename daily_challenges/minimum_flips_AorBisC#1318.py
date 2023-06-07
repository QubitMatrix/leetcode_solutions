class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a=bin(a)[2:]
        b=bin(b)[2:]
        c=bin(c)[2:]
        size=max(len(a),len(b),len(c))
        a="0"*(size-len(a))+a
        b="0"*(size-len(b))+b
        c="0"*(size-len(c))+c

        count=0
        for x in range(len(a)):
            if(c[x]=='1'):
                if(a[x]=='0' and b[x]=='0'):
                    count+=1
            else:
                if(a[x]=='1'):
                    count+=1
                if(b[x]=='1'):
                    count+=1
        return count
