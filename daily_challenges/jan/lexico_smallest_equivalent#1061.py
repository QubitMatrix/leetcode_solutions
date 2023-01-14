class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dic=defaultdict(set)
        used=[]
        count=0
        s=""
        for x in range(len(s1)):
            if(s1[x] not in used and s2[x] not in used):
                dic[count].add(s1[x])
                dic[count].add(s2[x])
                used.extend((s1[x],s2[x]))
                count+=1
            elif(s1[x] in used and s2[x] in used):
                for y in dic.keys():
                    if(s1[x] in dic[y]):
                        pos1=y
                        break
                for y in dic.keys():
                    if(s2[x] in dic[y]):
                        pos2=y
                        break
                if(pos1!=pos2):
                    dic[pos1]=dic[pos1].union(dic[pos2])
                    del dic[pos2]
                
            elif(s1[x] in used):
                for y in dic.keys():
                    if(s1[x] in dic[y]):
                        dic[y].add(s1[x])
                        dic[y].add(s2[x])
                        used.extend((s1[x],s2[x]))
            elif(s2[x] in used):
                for y in dic.keys():
                    if(s2[x] in dic[y]):
                        dic[y].add(s1[x])
                        dic[y].add(s2[x])
                        used.extend((s1[x],s2[x]))
        flag=0
        for x in baseStr:
            flag=0
            for y in dic.keys():
                if(x in dic[y]):
                    flag=1
                    s+=min(dic[y])
            if(flag==0):
                s+=x            
        return s
