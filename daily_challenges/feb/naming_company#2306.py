class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups=defaultdict(set)
        sum1=0
        for x in ideas:
            groups[x[0]].add(x[1:])
        for x in range(0,26):
            for y in range(x+1,26):
                s1=groups[chr(ord('a')+x)]
                s2=groups[chr(ord('a')+y)]
                s1_=s1-s2
                s2_=s2-s1
                sum1+=2*len(s1_)*len(s2_)
        return sum1
