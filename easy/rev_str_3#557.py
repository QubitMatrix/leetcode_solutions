class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        ss=""
        for x in s:
            ss+="".join(reversed(x))+" "
        return ss[:-1]
