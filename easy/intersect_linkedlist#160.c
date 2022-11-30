/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode* dheadB;
    while(headA!=NULL)
    {
        dheadB=headB;
        while(dheadB!=NULL)
        {
            if(dheadB==headA)
                return dheadB;
            dheadB=dheadB->next;
        }
        headA=headA->next;
    }
    return NULL;
}
