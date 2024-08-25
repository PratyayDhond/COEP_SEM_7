#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define NUM_KEYWORDS 32
#define NUM_OPERATORS 28
#define NUM_DIRECTIVES 6
#define NUM_SPECIALS 4

int getLength(char* token){
    int len = 0;
    char *cur = token;
    while(*cur != '\0'){
        cur++;
        len++;
    }
    return len;
}

const char* specialCharacters[NUM_SPECIALS] = {
    "(" , ")" , "{" , "}"
};

const char* keywords[NUM_KEYWORDS] = {
    "auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else",
    "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return",
    "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned",
    "void", "volatile", "while",
};

const char* preprocessor_directives[NUM_DIRECTIVES] = {
    "#define", "#undef", "#include", "#ifdef", "#ifndef", "#endif"
};

const char* operators[NUM_OPERATORS] = {
    "+", "-", "*", "/", "%", "++", "--", "=", "+=", "-=", "*=", "/=", "%=",
    "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!", "&", "|", "^", "~", "<<", ">>"
};

// Function to check if a string is a keyword
bool is_keyword(const char* str) {
    for (int i = 0; i < NUM_KEYWORDS; i++) {
        if (strcmp(str, keywords[i]) == 0) {
            return true;
        }
    }
    return false;
}

bool isPreprocessorDirective(const char* str) {
    for (int i = 0; i < NUM_DIRECTIVES; i++) {
        if (strcmp(str, preprocessor_directives[i]) == 0) {
            return true;
        }
    }
    return false;
}
// Function to check if a string is an operator
bool is_operator(const char* str) {
    for (int i = 0; i < NUM_OPERATORS; i++) {
        if (strcmp(str, operators[i]) == 0) {
            return true;
        }
    }
    return false;
}

bool isSpecialCharacter(const char* str){
    for(int i = 0; i < NUM_SPECIALS; i++){
        if (strcmp(str, specialCharacters[i]) == 0) {
            return true;
        }
    }
    return false;
}

// Function to determine the type of a string
const char* determine_type(const char* str) {
    if (is_keyword(str)) {
        return "KEYWORD";
    } else if (is_operator(str)) {
        return "OPERATOR";
    } else if( isPreprocessorDirective(str)){
        return "PREPROCESSOR DIRECTIVE";
    }else if( isSpecialCharacter(str)){
        return "BRACES";
    }else{
        return "IDENTIFIER";
    }
}

const char* getValue(const char* str){
    const char* type = determine_type(str);

    if(strcmp(type, "KEYWORD") == 0)
        return "Keyword";
    if(strcmp(type, "OPERATOR") == 0)
        return "Operator";
    if(strcmp(type, "PREPROCESSOR DIRECTIVE") == 0)
        return "Preprocessor directive";
    if(strcmp(type, "BRACES") == 0)
        return "Braces";

    else
        return "We have a value here";
}