from collections import defaultdict
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        minval=people[0]
        count=0
        dic=defaultdict(int)
        for x in people:
            dic[x]+=1
        for x in range(len(people)):
            if(dic[people[x]]==0):
                continue
            dic[people[x]]-=1
            ans=limit-people[x]
            while(ans>=minval and dic[ans]==0):
                ans-=1
            if(dic[ans]!=0):
                dic[ans]-=1
            count+=1
        return count
