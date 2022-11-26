class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen=len(min(strs,key=len))
        string=""
        s=""
        xx=0
        for x in range(minlen+1):
            for word in strs:
                if(not(word.startswith(string))):
                    xx=1
                    break
            if(xx==1):
                break
            s=string
            try:
                string+=strs[0][x]
            except:
                print(s,string,"a")
        return s
