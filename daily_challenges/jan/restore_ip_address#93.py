class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if(len(s)<4 or len(s)>12):
            return []
        lens=set(itertools.permutations([1,2,3]*4,4))
        print(len(lens))
        arr=[]
        for x in lens:
            if(sum(x)==len(s)):
                count=0
                st=""
                for y in x:
                    n=int(s[count:count+y])
                    if(len(str(n))==len(s[count:count+y])):
                        if(n<=255):
                            st+=str(n)+"."
                        else:
                            st=""
                            break
                    else:
                        st=""
                        break
                    count=count+y
                    
                if(st):
                    arr.append(st[:-1])
        return arr
