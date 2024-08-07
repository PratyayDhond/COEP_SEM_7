#include<stdio.h>
#include <stdlib.h>
#include <string.h>
#include "functions.h"
#define INITIAL_TOKEN_COUNT 10
#define MAX_TOKEN_LENGTH 256
#define DELIMITERS " ;\n"

int is_special_char(char c) {
    return c == '(' || c == ')' || c == '{' || c == '}';
}

// Function to tokenize the input string
char** getTokens(const char* input, int* token_count) {
    char** tokens = NULL;
    int token_capacity = INITIAL_TOKEN_COUNT;
    int token_index = 0;
    int inside_quotes = 0;
    int i = 0, j = 0;

    // Allocate initial memory for tokens
    tokens = (char**)malloc(token_capacity * sizeof(char*));
    if (!tokens) {
        perror("Failed to allocate memory");
        exit(EXIT_FAILURE);
    }

    // Initialize the first token
    tokens[token_index] = (char*)malloc(MAX_TOKEN_LENGTH * sizeof(char));
    if (!tokens[token_index]) {
        perror("Failed to allocate memory");
        exit(EXIT_FAILURE);
    }

    while (input[i] != '\0') {
        if (input[i] == '"') {
            inside_quotes = !inside_quotes; // Toggle inside_quotes flag
            tokens[token_index][j++] = input[i];
        } else if (is_special_char(input[i])) {
            if (j > 0) { // If we have a token to store before the special character
                tokens[token_index][j] = '\0';
                token_index++;
                
                // Allocate more memory if needed
                if (token_index >= token_capacity) {
                    token_capacity *= 2;
                    tokens = (char**)realloc(tokens, token_capacity * sizeof(char*));
                    if (!tokens) {
                        perror("Failed to reallocate memory");
                        exit(EXIT_FAILURE);
                    }
                }

                tokens[token_index] = (char*)malloc(MAX_TOKEN_LENGTH * sizeof(char));
                if (!tokens[token_index]) {
                    perror("Failed to allocate memory");
                    exit(EXIT_FAILURE);
                }
                j = 0;
            }
            // Store the special character as a separate token
            tokens[token_index][0] = input[i];
            tokens[token_index][1] = '\0';
            token_index++;
            
            // Allocate more memory if needed
            if (token_index >= token_capacity) {
                token_capacity *= 2;
                tokens = (char**)realloc(tokens, token_capacity * sizeof(char*));
                if (!tokens) {
                    perror("Failed to reallocate memory");
                    exit(EXIT_FAILURE);
                }
            }

            tokens[token_index] = (char*)malloc(MAX_TOKEN_LENGTH * sizeof(char));
            if (!tokens[token_index]) {
                perror("Failed to allocate memory");
                exit(EXIT_FAILURE);
            }
            j = 0;
        } else if (strchr(DELIMITERS, input[i]) && !inside_quotes) {
            if (j > 0) { // If we have a token to store
                tokens[token_index][j] = '\0';
                token_index++;
                
                // Allocate more memory if needed
                if (token_index >= token_capacity) {
                    token_capacity *= 2;
                    tokens = (char**)realloc(tokens, token_capacity * sizeof(char*));
                    if (!tokens) {
                        perror("Failed to reallocate memory");
                        exit(EXIT_FAILURE);
                    }
                }

                tokens[token_index] = (char*)malloc(MAX_TOKEN_LENGTH * sizeof(char));
                if (!tokens[token_index]) {
                    perror("Failed to allocate memory");
                    exit(EXIT_FAILURE);
                }
                j = 0;
            }
        } else {
            tokens[token_index][j++] = input[i];
        }
        i++;
    }
    
    // Store the last token if there is any
    if (j > 0) {
        tokens[token_index][j] = '\0';
        token_index++;
    }

    // Reallocate to shrink the size of the tokens array
    tokens = (char**)realloc(tokens, token_index * sizeof(char*));
    if (!tokens) {
        perror("Failed to reallocate memory");
        exit(EXIT_FAILURE);
    }

    *token_count = token_index;
    return tokens;
}

void freeTokens(char** tokens, int token_count) {
    for (int i = 0; i < token_count; i++) {
        free(tokens[i]);
    }
    free(tokens);
}


void print_tokens_table(char** codeTokens, int tokenCount) {
    printf("%-60s %-10s %-40s %-10s\n", "Lexeme", "Length", "Token", "Value/Address");
    printf("--------------------------------------------------------------------------------------------------------------------------\n");
    for (int i = 0; i < tokenCount; i++) {
        printf("%-60s %-10d %-40s %-10s\n", codeTokens[i], getLength(codeTokens[i]), determine_type(codeTokens[i]), getValue(codeTokens[i]));
    }
}


void printDetails(char* codeText){
    int tokenCount = 0;
    char** codeTokens = getTokens(codeText,&tokenCount);    

    print_tokens_table(codeTokens,tokenCount);

    freeTokens(codeTokens,tokenCount);
}
