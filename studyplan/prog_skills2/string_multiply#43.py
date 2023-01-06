class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        rem=0
        s=""
        if(not (int(num1) and int(num2))):
            return "0"
        for x in range(-1,-1*len(num1)-1,-1):
            for y in range(-1,-1*len(num2)-1,-1):
                a=int(num1[x])
                b=int(num2[y])
                c=a*b+rem
                q=c%10
                rem=c//10
                try:
                    q2=(int(s[y+x+1])+q)%10
                    rem=(int(s[y+x+1])+q)//10+rem
                    s=s[0:y+x+1]+str(q2)+s[y+x+2:]
                except Exception as e:
                    s=str(q)+s
            if(rem==0):
                continue
            try:
                z=len(s)
                s=s[0:-1*z]+str(int(s[-1*(z+1)])+rem)+s[y+x+1:]
            except Exception as e:
                s=str(rem)+s
                rem=0
        return(s)
