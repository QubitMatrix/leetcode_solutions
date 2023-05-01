class Solution:
    def average(self, salary: List[int]) -> float:
        sum1=0
        maxval=0
        minval=999999
        for x in salary:
            if(x>maxval):
                maxval=x
            if(x<minval):
                minval=x
            sum1+=x
        return (sum1-maxval-minval)/(len(salary)-2)
