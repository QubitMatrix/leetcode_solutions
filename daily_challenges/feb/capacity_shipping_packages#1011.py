class Solution:
    def check_shipping(self,w,days,weights):
        print(w)
        current=0
        days_count=1
        for x in weights:
            current+=x
            if(current>w):
                days_count+=1
                current=x
        return days_count<=days
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        h=sum(weights)
        while(l<=h):
            mid=(l+h)//2
            if(self.check_shipping(mid,days,weights)):
                ans=mid
                h=mid-1
            else:
                l=mid+1
        return ans
