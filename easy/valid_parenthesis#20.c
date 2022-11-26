struct node
{
    char token;
    struct node* next;
    struct node* prev;
};
typedef struct node node;
struct stack
{
    node *tail;
};
typedef struct stack stack;
node* pop(stack *s)
{
    node* tail;
    tail=s->tail;
    printf("tail%c",tail->token);
    if(s->tail!=NULL)
    {
        if(s->tail->prev!=NULL)
            s->tail->prev->next=NULL;
        s->tail=s->tail->prev;
    }
    return tail;
    
}
char oppbracket(char token)
{
    switch(token)
    {
        case ')': return '(';
        case ']': return '[';
        case '}': return '{';
        default: return 'x';
    }
}
bool isValid(char * ss){
    stack* s=malloc(sizeof(stack));
    s->tail=malloc(sizeof(node));
    s->tail->token='#';
    s->tail->next=s->tail->prev=NULL;
    int i=0;
    char token=ss[i];
    while(token!='\0')
    {
        node* newnode=malloc(sizeof(node));
        if(token=='(' || token=='['|| token=='{')
        {
            newnode->token=token;
            newnode->next=NULL;
            newnode->prev=NULL;
            s->tail->next=newnode;
            newnode->prev=s->tail;
            s->tail=s->tail->next;
            s->tail=newnode;
        }
        else
        {
            node* popped=pop(s);
            printf("pop:%c",popped->token);
            if(popped->token=='#')
                return false;//{}}
            else if(oppbracket(token)!=popped->token)//{]
                return false;
        }
            token=ss[++i];     
    }
    //printf("%c",s->tail->token);
    if(s->tail->prev==NULL)
        return true;//{}()
    else
        return false;//{}{
    
        
}
