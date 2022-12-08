/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 struct node
 {
     int val;
     struct node* next;
 };
 typedef struct node node;
void findleaves(node** head,struct TreeNode* root)
{
    if(root!=NULL)
    {
        if(root->left==NULL && root->right==NULL)
        {
            node* newnode=malloc(sizeof(node));
            newnode->val=root->val;
            newnode->next=NULL;
            if((*head)==NULL)
                *head=newnode;
            else
            {
                node* dhead=(*head);
                while(dhead->next!=NULL)
                {
                    dhead=dhead->next;
                }
                dhead->next=newnode;
            }
        }
        findleaves(head,root->left);
        findleaves(head,root->right);
    }
}
bool leafSimilar(struct TreeNode* root1, struct TreeNode* root2){
    node* head1=malloc(sizeof(node));
    head1=NULL;
    node* head2=malloc(sizeof(node));
    head2=NULL;
    findleaves(&head1,root1);
    findleaves(&head2,root2);
    node* dhead1=head1;
    node* dhead2=head2;
    while(dhead1!=NULL)
    {
        if(dhead2==NULL)
        return false;
        if(dhead1->val!=dhead2->val)
        return false;
        dhead1=dhead1->next;
        dhead2=dhead2->next;
    }
   return dhead2==NULL;
}
