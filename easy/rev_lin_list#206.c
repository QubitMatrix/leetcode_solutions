/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* new=malloc(sizeof(struct ListNode));
    new=NULL;
    while(head!=NULL)
    {
        struct ListNode* newnode=malloc(sizeof(struct ListNode));
        newnode->val=head->val;
        newnode->next=NULL;
        if(new==NULL)
        new=newnode;
        else
        {
            newnode->next=new;
            new=newnode;
        }
        head=head->next;
    }
    return new;
}
