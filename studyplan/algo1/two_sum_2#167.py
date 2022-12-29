class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1=index2=-1
        for x in range(len(numbers)):
            index1=x
            val=target-numbers[x]
            l=x+1
            h=len(numbers)
            while(l<=h):
                mid=(l+h)//2
                if(mid<len(numbers)):
                    if(numbers[mid]==val):
                        index2=mid
                        break
                    elif(numbers[mid]<val):
                        l=mid+1
                    else:
                        h=mid-1
                else:
                    break
            if(index2!=-1):
                break
        return list((index1+1,index2+1))
