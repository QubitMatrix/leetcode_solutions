/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
 int findmax(struct TreeNode*  root,int maxval)
 {
     int dif=0;
     int dif1=0;
     if(root!=NULL)
     {
         dif=root->val-maxval;
         if(dif<0)
         dif=dif*-1;
         dif1=findmax(root->left,maxval);
         if(dif1>dif)
         dif=dif1;
         dif1=findmax(root->right,maxval);
         if(dif1>dif)
         dif=dif1;
     }
     return dif;
 }
int maxAncestorDiff(struct TreeNode* root){
    int max=0;
    int max1=0;
    int maxret=0;
    if(root!=NULL)
    {
        maxret=findmax(root,root->val);
        if(maxret>max)
        max=maxret;
        max1=maxAncestorDiff(root->left);
        if(max1>max)
        max=max1;
        max1=maxAncestorDiff(root->right);
        if(max1>max)
        max=max1;
    }
    return max;

}
