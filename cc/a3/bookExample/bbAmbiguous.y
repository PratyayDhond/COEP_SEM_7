%{
#include<ctype.h>
#include<stdio.h>
#include<math.h>
double userDefinedVariables[1024];
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
line: VARIABLE ASSIGN expr {userDefinedVariables[$<id>1] = $3; printf("For DEBUG here: %f\n",userDefinedVariables[$<id>1]);}
    | expr '\n'     {$$ = $1; printf("%f\n",$1);}
    ;
expr: term ADD term            {$$=$1 + $3;}
    | term SUB term            {$$=$1 - $3;}
    | term                    {$$ = $1;}
    ;
term: factor MUL factor         {$$=$1 * $3;}
    | factor DIV factor         {$$=$1 / $3;}
    | factor MOD factor         {$$=$1 - (floor($1/$3) * $3);}
    | factor                    {$$ = $1;}
    ;
factor: OPEN_BR expr CLOSE_BR            {$$ = $2;}
      | num
      ;

%%
int main() {
    yyparse();
    return 0;
}

void yyerror(char *s) {
    fprintf(stderr, "error: %s\n", s);
    return;
}