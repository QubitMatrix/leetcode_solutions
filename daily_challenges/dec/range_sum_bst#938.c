/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int rangeSumBST(struct TreeNode* root, int low, int high){
    int sum1=0;
    if(root!=NULL)
    {
        if(root->val>low)
        sum1+=rangeSumBST(root->left,low,high);  
        if(root->val <=high && root->val >=low)
        {
            sum1+=root->val;
            printf("%d\n",sum1);
        }
        if(root->val<high)
        sum1+=rangeSumBST(root->right,low,high);
    }
    return sum1;
}
