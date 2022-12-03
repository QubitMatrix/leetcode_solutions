class Solution:
    def frequencySort(self, s: str) -> str:
        s1=""
        dic={}
        for x in s:
            if( x in dic.keys()):
                dic[x]+=1
            else:
                dic[x]=1
        l=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        for x in l:
            s1+=x[0]*x[1]
        return(s1)
