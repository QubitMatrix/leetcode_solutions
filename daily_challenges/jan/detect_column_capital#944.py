class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        dic={}
        for x in strs:
            for y in range(len(x)):
                if(y in dic.keys()):
                    dic[y].append(x[y])
                else:
                    dic[y]=[x[y]]
        count=0
        for x in dic.values():
            if(x!=sorted(x)):
                count+=1
        return count
