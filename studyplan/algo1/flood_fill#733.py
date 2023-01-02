class Solution:
    def dfs(self,image,srcx,srcy,arr,vis,val):
        arr.append((srcx,srcy))
        vis[srcx][srcy]=1
        if(srcx-1>=0 and vis[srcx-1][srcy]==0 and image[srcx-1][srcy]==val):
            self.dfs(image,srcx-1,srcy,arr,vis,image[srcx][srcy])
        if(srcy-1>=0 and vis[srcx][srcy-1]==0 and image[srcx][srcy-1]==val):
            self.dfs(image,srcx,srcy-1,arr,vis,image[srcx][srcy])
        if(srcx+1<len(image) and vis[srcx+1][srcy]==0 and image[srcx+1][srcy]==val):
            self.dfs(image,srcx+1,srcy,arr,vis,image[srcx][srcy])
        if(srcy+1<len(image[0]) and vis[srcx][srcy+1]==0 and image[srcx][srcy+1]==val):
            self.dfs(image,srcx,srcy+1,arr,vis,image[srcx][srcy])

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        arr=[]
        vis=[]
        t=[]
        for x in range(len(image)):
            vis.append([])
            for y in range (len(image[0])):
                t.append(0)
            vis[x]=t
            t=[]
        print(vis)

        self.dfs(image,sr,sc,arr,vis,image[sr][sc])
        print(arr)
        for x in arr:
            image[x[0]][x[1]]=color
        return image
