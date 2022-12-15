/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverse(struct ListNode* l)
{
    struct ListNode* ll=malloc(sizeof(struct ListNode));
    ll=NULL;
    struct ListNode* newnode;
    while(l!=NULL)
    {
        newnode=malloc(sizeof(struct ListNode));
        newnode->val=l->val;
        newnode->next=NULL;
        if(ll)
        {
            newnode->next=ll;
            ll=newnode;
        }
        else
        ll=newnode;
        l=l->next;
    }
    return ll;
} 
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    l1=reverse(l1);
    l2=reverse(l2);
    int num3=0;
    struct ListNode* l3=malloc(sizeof(struct ListNode));
    l3=NULL;
    struct ListNode* dl3=l3;
    int carry=0;
    int val=0;
    while(l1!=NULL && l2!=NULL)
    {
        num3=l1->val+l2->val+carry;
        carry=0;
        l1=l1->next;
        l2=l2->next;
        struct ListNode* newnode=malloc(sizeof(struct ListNode));
        newnode->val=num3%10;
        newnode->next=NULL;
        carry=num3/10;
        if(l3==NULL)
        {
            l3=newnode;
            dl3=l3;
        }
        else
        {
            dl3->next=newnode;
            dl3=dl3->next;
        }
    }
    while(l1!=NULL)
    {
        val=l1->val+carry;
        carry=0;
        struct ListNode* newnode=malloc(sizeof(struct ListNode));
        newnode->val=val%10;
        newnode->next=NULL;
        carry=val/10;
        if(l3==NULL)
        {
            l3=newnode;
            dl3=l3;
        }
        else
        {
            dl3->next=newnode;
            dl3=dl3->next;
        }
        l1=l1->next;
    }
    while(l2!=NULL)
    {
        val=l2->val+carry;
        carry=0;
        struct ListNode* newnode=malloc(sizeof(struct ListNode));
        newnode->val=val%10;
        newnode->next=NULL;
        carry=val/10;
        if(l3==NULL)
        {
            l3=newnode;
            dl3=l3;
        }
        else
        {
            dl3->next=newnode;
            dl3=dl3->next;
        }
        l2=l2->next;
    }
    if(carry!=0)
    {
        struct ListNode* newnode=malloc(sizeof(struct ListNode));
        newnode->val=carry;
        carry=0;
        newnode->next=NULL;
        if(l3==NULL)
        {
            l3=newnode;
            dl3=l3;
        }
        else
        {
            dl3->next=newnode;
            dl3=dl3->next;
        }
        
    }
    l3=reverse(l3);
    return l3;
}
