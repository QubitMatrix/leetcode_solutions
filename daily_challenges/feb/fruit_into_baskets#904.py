class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start=0
        maxfruits=0
        fruit1=-1
        fruit2=-1
        index1=-1
        index2=-1
        for x in range(len(fruits)):
            if(fruit1==fruits[x]):
                index1=x
                continue
            if(fruit2==fruits[x]):
                index2=x
                continue
            if(fruit1==-1):
                fruit1=fruits[x]
                index1=x
            elif(fruit2==-1):
                fruit2=fruits[x]
                index2=x
            else:
                maxfruits=max(maxfruits,x-start)
                #index1=len(f)-1-f[::-1].index(fruit1)
                #index2=len(f)-1-f[::-1].index(fruit2)
                index=min(index1,index2)
                if(index==index1):
                    index1=index2
                start=index+1
                fruit1=fruits[start]
                fruit2=fruits[x]
                index2=x
        maxfruits=max(maxfruits,len(fruits)-start)
        return maxfruits
