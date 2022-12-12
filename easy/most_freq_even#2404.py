class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic={}
        for x in nums:
            if(int(x)%2==0):
                try:
                    dic[x]+=1
                except:
                    dic[x]=1
        dic=sorted(dic.items(),key=lambda x:x[0])
        dic=sorted(dic,key=lambda x:x[1],reverse=True)
        if(dic==[]):
            return -1

        print(dic)
        return(dic[0][0])
