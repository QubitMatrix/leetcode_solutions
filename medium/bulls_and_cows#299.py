from collections import defaultdict
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic_s=defaultdict(int)
        dic_g=defaultdict(int)
        b=0
        c=0
        for x in range(len(secret)):
            dic_s[int(secret[x])]+=1
            dic_g[int(guess[x])]+=1
        for x in range(10):
            c+=min(dic_s[x],dic_g[x])
        for x in range(len(secret)):
            if(secret[x]==guess[x]):
                b+=1

        return(str(b)+'A'+str(c-b)+'B')
