int singleNumber(int* nums, int numsSize){
    int* arr=calloc(6*10*10*10*10,sizeof(int));
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]<0)
            arr[30000+nums[i]*(-1)]+=1;
        else
            arr[nums[i]]+=1;
    }
    for(int i=0;i<numsSize;i++)
    {
        if(nums[i]<0)
            printf("%d %d\n",nums[i],arr[30000+nums[i]*(-1)]);
        else
            printf("%d %d\n",nums[i],arr[nums[i]]);
        if(nums[i]<0 && arr[30000+nums[i]*(-1)]==1) 
            return nums[i];
        else if(nums[i]>=0 && arr[nums[i]]==1)
            return nums[i];

    }
    return -1;
    
}
