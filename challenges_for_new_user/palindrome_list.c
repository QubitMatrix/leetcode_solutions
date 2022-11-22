#include<string.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head){
int *arr1=malloc(sizeof(int)*100000);
int count1=0;
while(head!=NULL)
{
    arr1[count1]=head->val;
    printf("a%d\n",arr1[count1]);
    printf("%d",head->val);
    count1++;
    head=head->next;
}
    int *arr2=malloc(sizeof(int)*(count1));
    for(int i=0;i<(count1/2);i++)
    {
        if(arr1[i]!=arr1[count1-i-1])
            return false;
    }
    //printf("%s,%d",arr2,count1);
    return true;
}
