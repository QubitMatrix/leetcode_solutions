class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        l=sorted(zip(scores,ages))
        dic=[0]*(max(ages)+1)
        for s,a in l:
            dic[a]=s+max(dic[:a+1])
        return max(dic)
