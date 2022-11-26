int removeDuplicates(int* nums, int numsSize){
    for (int i=1;i<numsSize;i++)
    {
        if(nums[i]==1000)
            return i;
        if(nums[i]==nums[i-1])
        {
            printf("%d %d\n",i,nums[i-1]);
            for(int j=i;j<numsSize-1;j++)
            {
                nums[j]=nums[j+1];
                if(nums[j]==1000)
                    break;
            }
            nums[numsSize-1]=1000;
            i--;
        }
    }
    printf("a");
    return numsSize;
}
