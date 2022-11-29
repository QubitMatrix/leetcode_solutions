class Solution:
    def firstUniqChar(self, s: str) -> int:
        st=set()
        pos=set()
        dels=set()
        for x in range(len(s)):
            if(s[x] not in st and s[x] not in dels):
                st.add(s[x])
                pos.add(x)
            else:
                dels.add(s[x])
                try:
                    st.remove(s[x])
                    pos.remove(s.find(s[x]))
                except:
                    pass
        try:
            return(min(pos))
        except:
            return -1
