class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dic_num={}
        for x in nums:
            if(x in dic_num.keys()):
                dic_num[x]+=1
            else:
                dic_num[x]=1
        maxx=-1
        dic_num[-1]=0
        maxxarr=[]
        for x in dic_num:
            if(dic_num[x]>dic_num[maxx]):
                maxxarr=[]
                maxx=x
            if(dic_num[x]==dic_num[maxx]):
                maxxarr.append(x)
        num=nums.copy()
        num.reverse()
        minx=50000
        for x in maxxarr:
            stop=len(num)-1-num.index(x)
            start=nums.index(x)
            tot=stop+1-start
            if(tot<minx):
                minx=tot
        return minx
