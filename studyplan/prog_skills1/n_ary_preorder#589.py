/**
 * Definition for a Node.
 * struct Node {
 *     int val;
 *     int numChildren;
 *     struct Node** children;
 * };
 */

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct mynode
{
    struct Node* value;
    struct mynode* link;
};
typedef struct mynode mynode;
struct stack
{
    mynode* top;
};
typedef struct stack stack;
struct Node* pop(stack *st)
{
    struct Node* top=st->top->value;
    st->top=st->top->link;
    return top;
}
void push(stack* st,struct Node* root,struct Node* parent)
{
    //printf("%d\n",parent->numChildren);
    if(parent->numChildren==0)
    return;
    stack *new=malloc(sizeof(stack));
    new->top=NULL;
    int count=0;
    mynode *newnode;
    while(count<parent->numChildren)
    {
        newnode=malloc(sizeof(mynode));
        newnode->value=parent->children[count];
        newnode->link=NULL;
        if(new->top==NULL)
        new->top=newnode;
        else
        {
            mynode* top1=new->top;
            while(top1->link!=NULL)
            top1=top1->link;
            top1->link=newnode;
        }
        count++;
    }
    if(st->top!=NULL)
        newnode->link=st->top;
    st->top=new->top;
}
int* preorder(struct Node* root, int* returnSize) {
    int* arr=calloc(10000,sizeof(int));
    (*returnSize)=0;
    if(root==NULL)
    return arr;
    stack *st=malloc(sizeof(stack));
    st->top=malloc(sizeof(mynode));
    int size=0;
    mynode *temp=malloc(sizeof(mynode));
    temp->value=root;
    temp->link=NULL;
    st->top=temp;
    while(st->top!=NULL)
    {
        struct Node* t=pop(st);
        arr[size++]=t->val;
        (*returnSize)++;
        push(st,root,t);
    }
    return arr;
}
