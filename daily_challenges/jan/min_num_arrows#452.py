class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        stack=[]
        points.sort(key=lambda x:x[0])
        for s,e in points:
            if(stack!=[] and stack[-1][1]>=s):
                ps,pe=stack.pop()
                stack.append((max(s,ps),min(e,pe)))
            else:
                stack.append((s,e))
        return len(stack)
