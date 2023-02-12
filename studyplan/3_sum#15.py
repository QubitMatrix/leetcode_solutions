class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=[]
        p=[]
        z=[]
        for x in nums:
            if(x<0):
                n.append(x)
            if(x>0):
                p.append(x)
            if(x==0):
                z.append(x)
        l_n=len(n)
        l_p=len(p)
        l_z=len(z)
        s_n=set(n)
        s_p=set(p)
        s_s=set(nums)
        ans=set()
        if(l_z):
            for x in s_p:
                if(-1*x in s_n):
                    ans.add(tuple(sorted([-1*x,0,x])))
        if(l_z>=3):
            ans.add((0,0,0))
        if(l_p>1):
            for i in range(len(p)):
                for j in range(i+1,len(p)):
                    if(-1*(p[i]+p[j]) in s_n):
                        ans.add(tuple(sorted([p[i],p[j],-1*(p[i]+p[j])])))
        if(l_n>1):
            for i in range(len(n)):
                for j in range(i+1,len(n)):
                    if(-1*(n[i]+n[j]) in s_p):
                        ans.add(tuple(sorted([n[i],n[j],-1*(n[i]+n[j])])))
        return ans
            
