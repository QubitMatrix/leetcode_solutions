void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
int i2=0;
    //printf("%d %d\n",nums1Size,nums2Size);
for(int i=0;i<nums1Size;i++)
{
    if(i2<nums2Size && nums1[i]>nums2[i2])
    {
        for(int j=nums1Size-1;j>i;j--)
        {
            nums1[j]=nums1[j-1];
            //printf("%d\n",nums1[j]);
        }
        //printf("a");
        nums1[i]=nums2[i2];
        //printf("%d\n",nums1[i]);
        i2++;
    }
    else if(nums1[i]==0 && i>=nums1Size-nums2Size+i2)
    {
        //printf("b");
        nums1[i]=nums2[i2];
        i2++;
    }
    
}
}
