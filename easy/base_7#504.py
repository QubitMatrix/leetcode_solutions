class Solution:
    def convertToBase7(self, num: int) -> str:
        s=""
        n=int(num)
        if(n==0):
            return "0"
        if(n>0):
            while(n>0):
                s+=(str(n%7))
                n=n//7
            s=s[::-1]
        else:
            n=-1*n
            while(n>0):
                s=str(n%7)+s
                n=n//7
            s="-"+s
        return(s)
