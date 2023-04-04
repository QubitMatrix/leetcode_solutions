from collections import defaultdict
class Solution:
    def partitionString(self, s: str) -> int:
        dic=defaultdict(int)
        count=0
        for x in s:
            if(dic[x]==0):
                dic[x]+=1
            else:
                count+=1
                dic.clear()
                dic[x]+=1
        return(count+1)
