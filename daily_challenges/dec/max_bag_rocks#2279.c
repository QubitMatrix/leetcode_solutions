int cmp(const void* a,const void* b)
{
    return *(int*)a-*(int*)b;
}
int maximumBags(int* capacity, int capacitySize, int* rocks, int rocksSize, int additionalRocks){
    int d;
    int count=0;
    int counter=0;
    int arr[capacitySize];
    for (int i=0;i<capacitySize;i++)
    {
        d=capacity[i]-rocks[i];
        if(d==0)
        count+=1;
        else
        arr[counter++]=d;
    }
    qsort(arr,counter,4,cmp);
    for(int i=0;i<counter;i++)
    {
        if(additionalRocks>=arr[i])
        {
            additionalRocks-=arr[i];
            count+=1;
        }
    }
    return count;
}
