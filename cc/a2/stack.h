#define true 1
#define false 0

typedef struct Node{
    char* data;
    struct Node* next;
}Node;

typedef struct Stack{
    Node *top;
} Stack;


void initStack(Stack *s);
void push(Stack *s, char* data);
int isEmpty(Stack s);
char* pop(Stack *s);