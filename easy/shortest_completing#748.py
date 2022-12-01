class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        words.sort(key=len)
        a=[]
        dic_lic={}
        dic_word={}
        licensePlate=licensePlate.lower()
        for x in licensePlate:
            if(not x.isalpha()):
                continue
            if(x in dic_lic.keys()):
                dic_lic[x]+=1
            else:
                dic_lic[x]=1
        for x in words:
            x=x.lower()
            for y in x:
                if(y in dic_word.keys()):
                    dic_word[y]+=1
                else:
                    dic_word[y]=1
            for z in dic_lic.keys():
                try:
                    if(dic_lic[z]>dic_word[z]):
                        break
                
                    else:
                        a.append(z)
                except:
                    break
            if(set(a)==set(dic_lic.keys())):
                return x
            a=[]
            dic_word={}
