#ifndef SQL_PARSER_H
#define SQL_PARSER_H

#include <stdbool.h>

// Function to validate SQL query syntax
bool validate_sql_query(const char *query);

// Function to extract SQL keywords (like SELECT, INSERT, etc.)
void extract_sql_keywords(const char *query);

// Function to print syntax errors if any
void print_sql_error(const char *query);

#endif
