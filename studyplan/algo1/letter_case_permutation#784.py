class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n=len(s)
        range_arr=range(n)
        s=s.lower()
        posstr=set([s])
        s1=""
        for x in range(1,n+1):
            arr=itertools.combinations(range_arr,x)
            for y in arr:
                for z in range_arr:
                    if(z in y and s[z].isalpha()):
                        s1+=s[z].upper()
                    else:
                        s1+=s[z]
                posstr.add(s1)
                s1=""
        return posstr
