/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool exists(struct ListNode* node,int value)
{
    while(node!=NULL)
    {
        if(node->val==value)
            return true;
        node=node->next;
    }
    return false;
}
struct ListNode* deleteDuplicates(struct ListNode* head){
    struct ListNode *new=malloc(sizeof(struct ListNode));
    new=NULL;
    struct ListNode *dhead=head;
    struct ListNode *dnew;
    struct ListNode *newnode;
    while(dhead!=NULL)
    {
        newnode=malloc(sizeof(struct ListNode));
        newnode->val=dhead->val;
        newnode->next=NULL;
        if(new==NULL)
        {
            new=newnode;
            dnew=new;
        }
        else
        {
            if(!exists(new,dhead->val))
            {
                dnew->next=newnode;
                dnew=dnew->next;
            }
        }
        dhead=dhead->next;
    }
    return new;
}
