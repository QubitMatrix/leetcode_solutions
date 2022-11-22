class Solution:
    def romanToInt(self, s: str) -> int:
     try:
      print(len(s),s[0],s)
      arr=[]
      for x in s:
        if(x=='I'):
            arr.append(1)
        elif(x=='V'):
             arr.append(5)
        elif(x=='X'):
            arr.append(10)
        elif(x=='L'):
            arr.append(50)
        elif(x=='C'):
            arr.append(100)
        elif(x=='D'):
            arr.append(500)
        elif(x=='M'):
            arr.append(1000)
      x=1
      print(arr)
      sum_f=0
      while(x<len(arr)):
        if(arr[x-1]<arr[x]):
            sum_t=arr[x]-arr[x-1]
            x=x+1
        else:
            sum_t=arr[x-1]
        x=x+1
        sum_f+=sum_t
        print("a",sum_t)
      if(x==len(arr)):
        sum_f+=arr[x-1]
      print(sum_f)
     except:
      sum_f=0
      pass
     return sum_f
