class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_ind=10**6
        dic={}
        for x in range(len(list1)):
            for y in range(len(list2)):
                if(list1[x]==list2[y] and x+y<min_ind):
                    min_ind=x+y
                    dic[min_ind]=[]
                    dic[min_ind].append(list1[x])
                elif(list1[x]==list2[y] and x+y==min_ind):
                        dic[min_ind].append(list1[x])
        return dic[min_ind]
