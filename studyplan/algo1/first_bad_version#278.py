# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=0
        h=n
        x=-1
        while(l<=h):
            mid=(l+h)//2
            if(isBadVersion(mid)):
                  h=mid-1
                  x=mid
            else:
                l=mid+1
        return x
