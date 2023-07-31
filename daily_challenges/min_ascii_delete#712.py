def computecost(self,s1,s2,i,j,mem):
        if(i<0 and j<0):
            return 0
        if ((i,j) in mem):
            return mem[(i,j)]
        if(i<0):
            mem[(i,j)]=ord(s2[j])+computecost(s1,s2,i,j-1)
            return mem[(i,j)]
        
        if(j<0):
            mem[(i,j)]=ord(s1[i])+computecost(s1,s2,i-1,j)
            return mem[(i,j)]

        if(s1[i]==s2[j]):
            mem[(i,j)]=computecost(i-1,j-1)
            return mem[(i,j)]
        else:
            mem[(i,j)]=min(ord(s1[i])+computecost(s1,s2,i-1,j),ord(s2[j])+computecost(s1,s2,i,j-1))
            return mem[(i,j)]
