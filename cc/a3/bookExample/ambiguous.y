%{
#include<ctype.h>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<alloca.h>
#include<stddef.h>
extern FILE *yyin;

double userDefinedVariables[1024];
int yylex(void);
void yyerror(char *s)			
{      
    printf("%s\n",s);
}
%}


%union{
    double p;
    char id;
}
%token OPEN_BR CLOSE_BR ASSIGN
%token ADD SUB MUL DIV MOD
%token <id> VARIABLE
%token <p> num
%type <p> expr
%type <p> term
%type <p> factor
%type <p> line
%%

line: VARIABLE ASSIGN expr {userDefinedVariables[$1] = $3; printf("For DEBUG here: %f\n",userDefinedVariables[$1]);}
    | expr '\n'     {printf("%f\n",$1);}
    ;
expr: expr ADD term            {$$=$1 + $3;}
    | expr SUB term            {$$=$1 - $3;}
    | term
    ;
term: term MUL factor         {$$=$1 * $3;}
    | term DIV factor         {$$=$1 / $3;}
    | term MOD factor         {$$=$1 - (floor($1/$3) * $3);}
    | factor
    ;
factor: OPEN_BR expr CLOSE_BR            {$$ = $2;}
      | num
      ;

%%
void main() {
    printf("Scientific Calculator based on LEX YACC\n");
    yyin = stdin; // specify the input stream
    while(1){
        printf("Enter Expression: ");
        yyparse();
    }
}