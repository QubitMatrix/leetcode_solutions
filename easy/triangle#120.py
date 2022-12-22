class Solution:
    def triangle_min(self,triangle,dic,r,c):
        minn=triangle[r][c]
        str1=str(r)+"-"+str(c)
        if(str1 in dic.keys()):
            minn+=dic[str1]
        else:
            if(r==len(triangle)-1):
                return triangle[r][c]
            str2=str(r+1)+"-"+str(c)
            if(str2 not in dic.keys()):
                dic[str2]=self.triangle_min(triangle,dic,r+1,c)
            min1=dic[str2]
            str3=str(r+1)+"-"+str(c+1)
            if(str3 not in dic.keys()):
                dic[str3]=self.triangle_min(triangle,dic,r+1,c+1)
            min2=dic[str3]
            minn+=min(min1,min2)
        return minn
            

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dic={}
        return(self.triangle_min(triangle,dic,0,0))
