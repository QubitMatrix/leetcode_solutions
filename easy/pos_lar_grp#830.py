class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        pos=-1
        arr=[]
        while(1):
            pos+=1
            if(pos>=len(s)):
                break
            poss=pos
            while(1):
                poss+=1
                if(poss>=len(s)):
                    if(poss-pos>=3):
                        arr.append([pos,poss-1])
                    pos=poss-1
                    break
                if(s[poss]!=s[pos]):
                    if(poss-pos>=3):
                        arr.append([pos,poss-1])
                    pos=poss-1
                    break
                
        arr.sort(key=lambda x:x[0])
        return arr
