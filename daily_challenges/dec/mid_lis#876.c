/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head){
int count=0;
int count1=0;
struct ListNode* dhead=head;
struct ListNode* dhead2;
while(1)
{
    count++;
    while(dhead!=NULL && count1<count)
    {
        dhead=dhead->next;
        count1++;
    }
    if(dhead==NULL)
        break;
    dhead2=dhead;
    count1=0;
    while(dhead!=NULL && count1<count)
    {
        dhead=dhead->next;
        count1++;
    }
    if(count1==count && (dhead==NULL || dhead->next==NULL))
        return dhead2;
    count1=0;
    dhead=head;
}
    return head;
}
