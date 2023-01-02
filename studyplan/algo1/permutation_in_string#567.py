class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1={}
        dic2={}
        if(len(s1)>len(s2)):
            return False
        for x in s1:
            if(x in dic1.keys()):
                dic1[x]+=1
            else:
                dic1[x]=1
        for y in range(0,len(s1)):
                if(s2[y] in dic2.keys()):
                    dic2[s2[y]]+=1
                else:
                    dic2[s2[y]]=1
        d=s2[0]
        count=1
        if(dic1==dic2):
            return True
        for x in range(len(s1),len(s2),1):
            dic2[d]-=1
            if(dic2[d]==0):
                del dic2[d]
            if(s2[x] in dic2.keys()):
                dic2[s2[x]]+=1
            else:
                dic2[s2[x]]=1
            d=s2[count]
            count+=1
            print(dic1,dic2)
            if(dic1==dic2):
                return True
