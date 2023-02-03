class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s1=""
        if(numRows==1):
            return s
        for x in range(0,min(numRows,len(s))):
            s1+=s[x]
            present=x
            skip1=2*(numRows-x-1)
            skip2=2*x
            skip=skip1
            while((present+skip)<len(s)):
                if(skip!=0):
                    s1+=s[present+skip]
                    present=present+skip
                skip=skip1 if skip==skip2 else skip2
                print(x,s1,skip)

        return(s1)
