class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=""
        while(columnNumber>0):
            mod=columnNumber%26
            if(mod==0):
                s+='Z'
                mod=26
            else:
                s+=chr(mod+64)
            columnNumber=columnNumber-mod
            columnNumber=columnNumber//26
        s="".join(reversed(s))
        return s
