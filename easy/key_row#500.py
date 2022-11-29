class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1=set("qwertyuiop")
        r2=set("asdfghjkl")
        r3=set("zxcvbnm")
        arr=[]
        for x in words:
            s=set(x.lower())
            print(s,r1,r2,r3)
            if(s.issubset(r1) or s.issubset(r2) or s.issubset(r3)):
                arr.append(x)
        return arr
