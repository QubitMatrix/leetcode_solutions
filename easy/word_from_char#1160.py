class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        word={}
        sum1=0
        count=0
        char={}
        for x in chars:
            if(x in char.keys()):
                char[x]+=1
            else:
                char[x]=1
        for x in words:
            for y in x:
                if(y in word.keys()):
                    word[y]+=1
                else:
                    word[y]=1
            for z in word.keys():
                try:
                    if(word[z]>char[z]):
                        count=1
                        break
                except:
                    count=1
            if(count==1):
                count=0
            else:
                sum1+=len(x)
            word={}
        return sum1
