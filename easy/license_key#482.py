class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s1=s.split("-")
        s2="".join(s1)
        ref=""
        xx=0
        s2="".join(reversed(s2))
        for x in range(0,len(s2),k):
            if(x+k<=len(s2)):
                ref+=s2[x:x+k]+"-"
            xx=x
        if(xx!=len(s2)-k):
            ref+=s2[xx:]
        else:
            ref=ref[:len(ref)-1]
        s="".join(reversed(ref.upper()))
        print(s)
        return s
