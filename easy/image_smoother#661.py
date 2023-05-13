class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        sum1=0
        count=0
        l=[]
        mat=[]
        for x in range(len(img)):
            for y in range(len(img[0])):
                l.append(0)
            mat.append(l)
            l=[]
        for x in range(len(img)):
            for y in range(len(img[0])):
                if(y>0):
                    sum1+=img[x][y-1]
                    count+=1
                    if(x>0):
                        sum1+=img[x-1][y-1]
                        count+=1
                    if(x<len(img)-1):
                        sum1+=img[x+1][y-1]
                        count+=1
                if(y<len(img[0])-1):
                    sum1+=img[x][y+1]
                    count+=1
                    if(x>0):
                        sum1+=img[x-1][y+1]
                        count+=1
                    if(x<len(img)-1):
                        sum1+=img[x+1][y+1]
                        count+=1
                if(x>0):
                    sum1+=img[x-1][y]
                    count+=1
                if(x<len(img)-1):
                    sum1+=img[x+1][y]
                    count+=1
                sum1+=img[x][y]
                count+=1
                avg=sum1//count
                mat[x][y]=avg
                sum1=0
                count=0
        return mat
