#include <stdio.h>
#include <stdlib.h>
#include "file.h"
#include "analyser.h"

int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file_path>\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char* file_path = argv[1];
    char* codeText = read_file_contents(file_path);

    if (codeText) {
        printDetails(codeText);
        printLexErrors(codeText);
    } else {
        fprintf(stderr, "Failed to read file or file does not exist.\n");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}


// TODO
/*
A lexical error is a sequence of characters that does not match the pattern of any token
Add Lexical Error analysis
*/