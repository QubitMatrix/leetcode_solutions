class Solution:
    def myAtoi(self, s: str) -> int:
        count=0
        s1=""
        for x in s:
            if(count==0 and x.isspace()):
                continue
            elif(x.isnumeric()):
                count=1
                s1+=x
            elif(count==0 and (x=='+' or x=="-")):
                count=1
                s1+=x
            else:
                break
        try:
            if(int(s1)>2**31-1):
                return 2**31-1
            elif(int(s1)<-2**31):
                return -2**31
            else:
                return (int(s1))
        except:
            return(0)
