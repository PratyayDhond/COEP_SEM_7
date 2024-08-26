%{
#include<stdio.h>

int keywordCount = 0;
int identifierCount = 0;
int operatorCount = 0;
int commentCount = 0;
int headerCount = 0;
int singleLinedCommentCount = 0;
int multiLinedCommentCount = 0;
int preprocessorDirectiveCount = 0;
int lineNumber = 0;
%}

%%
\n {lineNumber++;}
"//".* {singleLinedCommentCount++; commentCount++;}
"/*".*"*/" {multiLinedCommentCount++; commentCount++;}
[ \t]+ ;

#(include|define|undef|if|ifdef|ifndef|else|elif|endif|error|pragma|line) { printf("Preprocessor Directive --> %s\n", yytext); preprocessorDirectiveCount++; }
"<".*.h> {printf("Header File -> %s\n", yytext);headerCount++;}

(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|int|long|register|return|short|signed|sizeof|static|switch|typedef|union|unsigned|void|volatile|while) { printf("Keyword --> %s\n", yytext); keywordCount++; }

[a-zA-Z][a-zA-Z0-9_]* {printf("Identifier --> \'%s\'\n", yytext); identifierCount++;}
-?[0-9]+(\.[0-9]+)? {printf("Number --> %s\n", yytext);}
\"[^\"\n]*\" { printf("String literal -> %s\n", yytext); }

(\+|\-|\*|\/|\%|==|!=|>|<|>=|<=|&&|\|\||!|\&|\||\^|~|<<|>>|=|\+=|\-=|\*=|\/=|%=|\&=|\|=|\^=|<<=|>>=|\+\+|\-\-|\?\:|\,|\&|\.|\->) {printf("Operator --> `%s`\n", yytext);}

(\(|\)|\{|\}|\[|\]|\;|\,|\.|\->) {printf("Symbol --> `%s`\n", yytext);}

.       { printf("Lexical Error at line %d at `%s`\n", lineNumber, yytext); }
%%

int main(int argc, char** argv){
	if(argc > 1){ // there were commandline arguments provided
		FILE *fptr = fopen(argv[1], "r");
		if(!fptr){
			perror("File pointer error! File couldn't be opened and accessed");
			return 1;
		}
		yyin = fptr; // yyin is defined by lex by default
		// if you don't assign yyin; then yyin is set to stdin by default
		// so if you assign yyin here, it will read from the file
		// if there are no arguments given to the main method through the console
		// the stdin would be the input stream for the process.
	}
	yylex();
	printf("Number of Pre-Processor Directives : %d\n", preprocessorDirectiveCount);
	printf("Number of Headers : %d\n", headerCount);
	printf("Number of Keywords : %d\n", keywordCount);
	printf("Number of Identifiers : %d\n", identifierCount);
	printf("Number of Operators : %d\n", operatorCount);
	printf("Number of Comments : %d\n", commentCount);
	printf("Number of // Comments : %d\n", singleLinedCommentCount);
	printf("Number of /* Comments : %d\n", multiLinedCommentCount);
	printf("Number of Lines : %d\n", lineNumber);
	return 0;
}
