/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val){
    struct ListNode* del;
    while(1)
    {
        if(head==NULL)
            return head;
        if(head->val==val)
        {    
            del=head;
            head=head->next;
            free(del);
        }
        else
            break;
    }
    
    struct ListNode* prev;
    struct ListNode* dhead=head;
    prev=NULL;
    while(dhead!=NULL)
    {
         if(dhead->val==val)
         {
             del=dhead;
             prev->next=dhead->next;
             dhead=dhead->next;
             free(del);
         }
         else
         {
             prev=dhead;
             dhead=dhead->next;
         }   
    }
    return head;
}
