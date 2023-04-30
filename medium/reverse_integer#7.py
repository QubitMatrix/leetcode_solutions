class Solution:
    def reverse(self, x: int) -> int:
        flag=0
        if(x>0):
            s="".join(reversed(str(x)))
        else:
            flag=1
            s="".join(reversed(str(-1*x)))
        return 0 if(int(s)>2**31-1 or int(s)<-1*2**21) else int(s) if flag==0 else -1*int(s)
