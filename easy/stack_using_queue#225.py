from queue import Queue
class MyStack:

    def __init__(self):
        self.q=Queue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        l=self.q.qsize()
        count=1
        while(count<l):
            self.q.put(self.q.get())
            count+=1
        return self.q.get()
    def top(self) -> int:
        l=self.q.qsize()
        count=1
        while(count<=l):
            ans=self.q.get()
            self.q.put(ans)
            count+=1
        return ans

    def empty(self) -> bool:
        return(self.q.empty())


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
