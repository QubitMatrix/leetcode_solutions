class Solution:
    def merge(self,nums,low,mid,high):
        i=low
        j=mid+1
        t=[]
        while(i<=mid and j<=high):
            if(nums[i]<=nums[j]):
                t.append(nums[i])
                i+=1
            else:
                t.append(nums[j]) 
                j+=1
        while(i<=mid):
            t.append(nums[i])
            i+=1
        while(j<=high):
            t.append(nums[j])
            j+=1
        nums[low:high+1]=t   
        
    def mergesort(self,nums,low,high):
        if(low!=high):
            mid=(low+high)//2
            self.mergesort(nums,low,mid)
            self.mergesort(nums,mid+1,high)
            self.merge(nums,low,mid,high)    
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums
