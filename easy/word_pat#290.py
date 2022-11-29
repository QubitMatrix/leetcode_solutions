class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        alp=[]
        encode={}
        encode_pat={}
        count=0
        s1=""
        s2=""
        for x in range(26):
            alp.append(chr(x+97))
        words=s.split(" ")
        for x in words:
            if(x not in encode.keys()):
                encode.update({x:alp[count]})
                count+=1
        print(encode)
        count=0
        for x in pattern:
            if(x not in encode_pat.keys()):
                encode_pat.update({x:alp[count]})
                count+=1
        print(encode_pat)
        for x in words:
            s1+=encode[x]
        print(s1)
        for x in pattern:
            s2+=encode_pat[x]
        print(s1,s2)
        return s1==s2
