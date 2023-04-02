class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        dic={}
        potions.sort()
        maxval=potions[-1]
        count=0
        suc=[]
        for x in range(len(potions)):
            if(potions[x] not in dic):
                dic[potions[x]]=len(potions)-count
            count+=1
        for x in spells:
            ans=math.ceil(success/x)
            if(ans>maxval):
                suc.append(0)
                continue
            while(ans not in dic):
                ans+=1
            suc.append(dic[ans])
        return(suc)
