class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        arr=[]
        count_dic=defaultdict(int)
        check_dic=defaultdict(int)
        if(len(s)<len(p)):
            return []
        for x in p:
            count_dic[x]+=1
        for x in range(len(p)):
            check_dic[s[x]]+=1
        delete=s[0]
        counter=0
        start=0
        if(count_dic==check_dic):
            arr.append(start)
        for x in range(len(p),len(s)):
            check_dic[s[x]]+=1
            check_dic[delete]-=1
            if(check_dic[delete]==0):
                del check_dic[delete]
            counter+=1
            delete=s[counter]
            if(check_dic==count_dic):
                arr.append(counter)
        return arr
