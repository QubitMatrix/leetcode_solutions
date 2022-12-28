/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode *list3=malloc(sizeof(struct ListNode));
    list3=NULL;
    struct ListNode *dhead=list3;
    struct ListNode* newnode;
    while(list1!=NULL && list2!=NULL)
    {
        if(list1->val<list2->val)
        {
            newnode=malloc(sizeof(struct ListNode));
            newnode->val=list1->val;
            newnode->next=NULL;
            if(list3==NULL)
            {
                list3=newnode;
                dhead=list3;
            }
            else
            {
                dhead->next=newnode;
                dhead=dhead->next;
            }
            list1=list1->next;
        }
        else
        {
            newnode=malloc(sizeof(struct ListNode));
            newnode->val=list2->val;
            newnode->next=NULL;
            if(list3==NULL)
            {
                list3=newnode;
                dhead=list3;
            }
            else
            {
                dhead->next=newnode;
                dhead=dhead->next;
            }
            list2=list2->next;
        }
    }
    while(list1!=NULL)
    {
        newnode=malloc(sizeof(struct ListNode));
        newnode->val=list1->val;
        newnode->next=NULL;
        if(list3==NULL)
        {
            list3=newnode;
            dhead=list3;
        }
        else
        {
            dhead->next=newnode;
            dhead=dhead->next;
        }
        list1=list1->next;
    }
    while(list2!=NULL)
    {
        newnode=malloc(sizeof(struct ListNode));
        newnode->val=list2->val;
        newnode->next=NULL;
        if(list3==NULL)
        {
            list3=newnode;
            dhead=list3;
        }
        else
        {
            dhead->next=newnode;
            dhead=dhead->next;
        }
        list2=list2->next;
    }
    return list3;
}
