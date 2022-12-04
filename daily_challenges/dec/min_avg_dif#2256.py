class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        sum1=0
        sum2=sum(nums)
        for x in range(n):
            sum1+=nums[x]
            avg1=sum1//(x+1)
            try:
                sum2-=nums[x]
                avg2=sum2//(n-x-1)
            except:
                avg2=0
            dif=math.fabs(avg1-avg2)
            dic[x]=int(dif)
        dic=sorted(dic.items(),key=lambda x:x[1])
        minn=dic[0][1]
        l=list(map(lambda x:x[0],filter(lambda x:x[1]==minn,dic)))
        l.sort()
        return(l[0])
