class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count=0
        if(s1==s2):
            return True
        for x in range(len(s1)):
            if(count==0 and s1[x]!=s2[x]):
                a=x
                count+=1
            elif(count==1 and s1[x]!=s2[x]):
                b=x
                count+=1
            elif(count>1 and s1[x]!=s2[x]):
                return False
        return (count==2 and s1[a]==s2[b] and s2[a]==s1[b])
