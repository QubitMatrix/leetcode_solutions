class Solution:
    def countSegments(self, s: str) -> int:
        if(s==""):
            return 0
        s=s.split()
        return len(s)
