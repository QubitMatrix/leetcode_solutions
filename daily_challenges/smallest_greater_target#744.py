class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l=0
        h=len(letters)
        s=""
        while(l<=h):
            mid=(l+h)//2
            if(mid>=len(letters)):
                break
            if(target<letters[mid]):
                s=letters[mid]
                h=mid-1
            else:
                l=mid+1
        if(s):
            return s
        else:
            return letters[0]
