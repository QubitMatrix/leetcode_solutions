class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=title.split()
        s1=""
        for x in l:
            if(len(x)<=2):
                x=x.lower()
                s1+=x+" "
            else:
                x=x.lower()
                s1+=x[0].upper()+x[1:]+" "
        return s1[:-1]
