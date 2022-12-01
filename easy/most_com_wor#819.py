import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic={}
        paragraph=paragraph.lower()
        para=re.split("\W+",paragraph)
        print(para)
        try:
            para.remove("")
        except:
            pass
        for x in para:
            if(x not in banned):
                if(x in dic.keys()):
                    dic[x]+=1
                else:
                    dic[x]=1
        print(dic)
        maxval=max(list(dic.values()))
        for x in dic.keys():
            if(dic[x]==maxval):
                return x
