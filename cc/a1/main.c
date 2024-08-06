#include <stdio.h>
#include <stdlib.h>
#include "fileReader.h"

int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <file_path>\n", argv[0]);
        return EXIT_FAILURE;
    }

    const char* file_path = argv[1];
    char* content = read_file_contents(file_path);

    if (content) {
        printf("File Contents:\n%s\n", content);
        free(content); // Remember to free the allocated memory
    } else {
        fprintf(stderr, "Failed to read file or file does not exist.\n");
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
