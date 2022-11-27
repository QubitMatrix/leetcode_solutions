/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q){
bool x=true;
bool xx;
if(p!=NULL && q!=NULL)
{
    if(p->val!=q->val)
        return false;
    x=isSameTree(p->left,q->left);
    xx=isSameTree(p->right,q->right);
    if(x==false ||xx==false)
        x=false;
}
else
{
    if(p!=NULL && q==NULL || p==NULL && q!=NULL)
        return false;
}

return x;
}
