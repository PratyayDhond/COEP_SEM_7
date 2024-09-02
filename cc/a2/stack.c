#include<stdio.h>
#include<stdlib.h>
#include<limits.h>
#include "stack.h"
#include<string.h>
#include "functions.h"

void initStack(Stack *s){
    s->top = NULL;
}


Node* newNode(char* data){
    Node *nn = (Node*) malloc(sizeof(Node));
    nn->data = (char*) malloc(sizeof(char) * getLength(data));
    strcpy(nn->data, data);
    nn ->next = NULL;
    return nn;
}

void push(Stack *s, char* data){
    Node *nn = newNode(data);
    if(!nn){
        perror("Internal Error at STACK! MALLOC FAILURE!");
        exit(1);
    }
    if(s->top == NULL)
        s->top = nn;
    else{
        nn->next = s->top;
        s->top = nn;
    }
}

int isEmpty(Stack s){
    if(s.top == NULL)
        return 1;
    return 0;
}

char* pop(Stack *s){
    if(isEmpty(*s)){
        return "$";
    }

    Node * temp = s->top;
    s->top = s->top->next;
    char* returnValue = temp->data;
    free(temp);
    return returnValue;
}