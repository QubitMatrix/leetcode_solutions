class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        arr=[]
        count=0
        minstr=min(words,key=len)
        for x in range(len(minstr)):
            char=minstr[x]
            for y in words:
                if(char not in y):
                    count=1
                    break
                else:
                    pos=y.index(char)
                    poss=words.index(y)
                    y=y[0:pos]+y[pos+1:]
                    words[poss]=y
            if(count==1):
                count=0
            else:
                arr.append(char)
        return arr
