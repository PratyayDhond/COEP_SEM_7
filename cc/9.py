import re
from sympy import simplify, symbols


import re

def common_subexpression_elimination(code):
    """
    Optimizes code by eliminating common subexpressions.

    Args:
        code (str): C-like code as a string.

    Returns:
        str: Optimized code with common subexpressions eliminated.
    """
    lines = code.split("\n")
    optimized_code = []
    expressions = {}  # Dictionary to store common subexpressions

    for line in lines:
        line = line.strip()
        if not line or ";" not in line:  # Skip empty lines or non-statements
            optimized_code.append(line)
            continue

        # Match expressions of the form `a = b + c;`
        match = re.match(r"(\w+)\s*=\s*([^;]+);", line)
        if match:
            var, expr = match.groups()
            expr = expr.strip()

            # Check if the expression has been computed before
            if expr in expressions:
                # Replace with existing variable
                optimized_code.append(f"{var} = {expressions[expr]};")
            else:
                # Add the expression to the dictionary
                expressions[expr] = var
                optimized_code.append(line)
        else:
            optimized_code.append(line)

    return "\n".join(optimized_code)


def strength_reduction(code):
    """
    Replaces expensive operations with equivalent cheaper ones in the given code.

    Args:
        code (str): Input code as a string.

    Returns:
        str: Optimized code with strength reduction applied.
    """
    lines = code.strip().split("\n")
    optimized_code = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Match multiplication by 2, 4, 8, etc.
        match_mul = re.search(r"(\w+)\s*=\s*(\w+)\s*\*\s*(\d+)\s*;", line)
        if match_mul:
            var, operand, multiplier = match_mul.groups()
            multiplier = int(multiplier)
            if (multiplier & (multiplier - 1)) == 0:  # Check if multiplier is a power of 2
                shift_amount = multiplier.bit_length() - 1
                optimized_code.append(f"{var} = {operand} << {shift_amount};")
                continue

        # Match division by 2, 4, 8, etc.
        match_div = re.search(r"(\w+)\s*=\s*(\w+)\s*/\s*(\d+)\s*;", line)
        if match_div:
            var, operand, divisor = match_div.groups()
            divisor = int(divisor)
            if (divisor & (divisor - 1)) == 0:  # Check if divisor is a power of 2
                shift_amount = divisor.bit_length() - 1
                optimized_code.append(f"{var} = {operand} >> {shift_amount};")
                continue

        # If no optimization applies, keep the original line
        optimized_code.append(line)

    return "\n".join(optimized_code)



def code_hoisting(code):
    lines = code.split("\n")
    optimized_code = []
    hoisted_code = []
    repeated_expressions = {}
    var_hoisted =[]

    # Step 1: Identify repeated expressions in both if and else blocks
    for line in lines:
        stripped_line = line.strip()

        match = re.match(r"(\w+)\s*=\s*([^;]+);", stripped_line)
        if match:
            var, expr = match.groups()
            expr = expr.strip()

            # Track repeated expressions
            if expr in repeated_expressions:
                repeated_expressions[expr].append(var)
            else:
                repeated_expressions[expr] = [var]

    # Step 2: Hoist repeated expressions above the blocks
    for expr, vars_used in repeated_expressions.items():
        if len(vars_used) > 1:  # Only hoist if the expression is used more than once
            hoisted_code.append(f"temp = {expr};")
            for var in vars_used :
               if var not in var_hoisted:
                 hoisted_code.append(f"{var} = temp;")
                 var_hoisted.append(var)

    # Step 3: Rebuild the code and replace the expressions with 'temp'
    final_code = []
    inside_if = False
    inside_else = False

    for line in lines:
        stripped_line = line.strip()

        # Detect if or else blocks
        if "if" in stripped_line:
            inside_if = True
            final_code.append(stripped_line)
            continue
        elif "else" in stripped_line:
            inside_else = True
            final_code.append(stripped_line)
            continue

        # Replace repeated expressions with 'temp'
        match = re.match(r"(\w+)\s*=\s*([^;]+);", stripped_line)
        if match:
            var, expr = match.groups()
            expr = expr.strip()

            if expr in repeated_expressions and len(repeated_expressions[expr]) > 1:
                line = line.replace(f"{var} = {expr};", f"")

        final_code.append(line)

    # Step 4: Insert hoisted code at the beginning of the final code
    final_code = hoisted_code + final_code

    return "\n".join(final_code)

import re


def constant_folding(c_code):
    # Regular expression to match expressions like: 'x + 2', '5 * y', '3 + 4', etc.
    pattern = re.compile(r'([0-9]+)\s*([\+\-\*/\^])\s*([0-9]+)')
    
    def fold_expression(match):
        """Helper function to simplify constant expressions."""
        left_operand = int(match.group(1))
        operator = match.group(2)
        right_operand = int(match.group(3))
        
        if operator == '+':
            return str(left_operand + right_operand)
        elif operator == '-':
            return str(left_operand - right_operand)
        elif operator == '*':
            return str(left_operand * right_operand)
        elif operator == '/':
            return str(left_operand // right_operand)  # Assume integer division
        elif operator == '^':  # Handling exponentiation
            return str(left_operand ** right_operand)
    
    # Function to optimize constant expressions
    optimized_code = c_code
    
    # Loop to find and replace constant expressions in the code
    while re.search(pattern, optimized_code):
        optimized_code = re.sub(pattern, fold_expression, optimized_code)
   
    return optimized_code





def dead_code_elimination(code):
    """
    Removes unused variables from the code.
    """
    lines = code.strip().split("\n")
    used_vars = set()
    # Detect used variables
    for line in lines:
        matches = re.findall(r"\b\w+\b", line)
        if len(matches) > 1:
            used_vars.update(matches[1:])  # Collect RHS variables
    
    optimized_code = []
    for line in lines:
        if "=" in line:
            var = line.split("=")[0].strip()  # LHS variable
            if var in used_vars:
                optimized_code.append(line)
        else:
            optimized_code.append(line)
    
    return "\n".join(optimized_code)

def optimize_c_code(c_code):
    OG_code = c_code
    """
    Optimizes the provided C code and outputs the results.
    """
    print("Original Code:\n", OG_code, "\n")
    # Step 3: Code hOISTING
    c_code = code_hoisting(c_code)
    c_code3 = code_hoisting(OG_code)
    print("Optimized Code by Code Hoisting:\n", c_code3)
    # Step 1: Constant folding and propagation
    c_code = constant_folding(c_code)
    c_code1 = constant_folding(OG_code)
    print("Optimized Code by Constant Folding:\n", c_code1)
    # Step 2: Dead code elimination
    c_code = dead_code_elimination(c_code)
    c_code2 = dead_code_elimination(OG_code)
    print("Optimized Code by Dead Code Elimination:\n", c_code2)
    #Step 4:StrengthReduction
    c_code = strength_reduction(c_code)
    c_code4 = strength_reduction(OG_code)
    print("Optimized Code by StrengthReduction:\n", c_code4)

    #Step 5: Common Subexpression
    c_code = common_subexpression_elimination(c_code)
    c_code5 = common_subexpression_elimination(OG_code)
    print("Optimized Code by Common Subexpression:\n", c_code5)
    # Print optimized code
    print("Optimized Code:\n", c_code)

# Input: Basic C code for optimization
c_code =  """


r = 2 + 9 ; // folding

if (TRUE) {
    a = b + c; // common subexpression
    d = b + c; // common subexpression
    m = b ** c; // Deadcode
    e = a * 2; // Strength reduction
    f = d + r;
} else {
    a = b + c;
    d = b + c;
    e = a / 4; // Strength reduction
    f = d - r;
}
printf(e);
printf(f);

"""

optimize_c_code(c_code)





























"""
Example Code1:
a = 5 + 3;
b = a + 7;
printf("b")

Example Code2:
if (i == 0)
{
    a = b + c;
    d = b + c;
    e = a * 2;
    f = b + c;
}
else
{
    a = b + c;
    d = b + c;
    e = a - 2;
    f = b - c;
}

Example Code3:

 a = b * 2;
 c = d / 4;
 e = f * 5;  // This won't be optimized
 g = b * 2;
 
 Example Code4:
 g = 2 + 8
 r = g - 18 //constant propogation 
 if (i == 0)
{
    a = b + c;//common subexpression
    d = b + c;//common subexpression
    m = b **c; //Deadcode
    e = a * 2;//Strength reduction
    f = d + r;// constant propogation
}
else
{
    a = b + c;
    d = b + c;
    e = a / 4;//Strength reduction
    f = d - r;//constant propogation
}
printf(e)
printf(f)



"""
