/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* oddEvenList(struct ListNode* head){
    struct ListNode *dhead=head;
    struct ListNode *tail,*dtail,*end;
    int count=0;
    if(head==NULL)
    return NULL;
    while(dhead!=NULL)
    {
        if(count%2==0)
        tail=dhead;
        end=dhead;
        dhead=dhead->next;
        count++;
        
    }
    dtail=tail;
    dhead=head;
    //even=dhead->next;
    while(dhead!=dtail)
    {
        tail->next=dhead->next;
        dhead->next=dhead->next->next;
        dhead=dhead->next;
        tail=tail->next;
    }
    if(dtail!=end)
    {
        tail->next=end;
        tail=tail->next;
    }
    tail->next=NULL;
    return head;
}
