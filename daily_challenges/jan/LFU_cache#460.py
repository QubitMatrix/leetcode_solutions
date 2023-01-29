class LFUCache:

    def __init__(self, capacity: int):
        self.size=capacity
        self.hash={}
        self.q=[]
        self.freq=defaultdict(set)

    def get(self, key: int) -> int:
        if(key in self.hash):
            self.q.remove(key)
            self.q=[key]+self.q
            self.freq[self.hash[key][1]].remove(key)
            if(not self.freq[self.hash[key][1]]):
                del self.freq[self.hash[key][1]]
            self.hash[key][1]+=1
            self.freq[self.hash[key][1]].add(key)
            return self.hash[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.hash):
            self.hash[key][0]=value
            self.freq[self.hash[key][1]].remove(key)
            if(not self.freq[self.hash[key][1]]):
                del self.freq[self.hash[key][1]]
            self.hash[key][1]+=1#frequency
            self.freq[self.hash[key][1]].add(key)            
            self.q.remove(key)
            self.q=[key]+self.q
        else:
            if(self.size==0):
                return
            if(len(self.hash)==self.size):
                minn=min(self.freq.keys())
                if(len(self.freq[minn])==1):
                    a=self.freq[minn].pop()
                    self.q.remove(a)
                    del self.hash[a]
                    del self.freq[minn]

                else:
                    t=self.freq[minn]
                    for xx in self.q[::-1]:
                        if(xx in t):
                            self.freq[minn].remove(xx)
                            del self.hash[xx]
                            self.q.remove(xx)
                            pos=xx
                            break

                self.q=[key]+self.q
                self.hash[key]=[value,1]
                self.freq[1].add(key)

            else:
                self.hash[key]=[value,1]
                self.freq[1].add(key)
                self.q=[key]+self.q



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
