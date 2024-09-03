import sys
sys.setrecursionlimit(60) # to avoid stack_overflow and long recursions
 
def first(current_token):
    first_ = set()
    if current_token in non_terminals:
        possible_unit_productions = productions_dict[current_token]

        for unit_production in possible_unit_productions:
            first_2 = first(unit_production)
            first_ = first_ |first_2 # merging the two sets by OR operation

    elif current_token in terminals:
        first_ = {current_token}

    elif current_token=='' or current_token=='ε':
        first_ = {'ε'}

    else:
        first_2 = first(current_token[0])
        if 'ε' in first_2:
            i = 1
            while 'ε' in first_2:
                first_ = first_ | (first_2 - {'ε'})
                if current_token[i:] in terminals:
                    first_ = first_ | {current_token[i:]}
                    break
                elif current_token[i:] == '':
                    first_ = first_ | {'ε'}
                    break
                first_2 = first(current_token[i:])
                first_ = first_ | first_2 - {'ε'}
                i += 1
        else:
            first_ = first_ | first_2

    return  first_


def follow(non_terminal_token):
    follow_ = set()
    prods = productions_dict.items()
    if non_terminal_token==starting_symbol:
        follow_ = follow_ | {'$'}
    for non_terminal,right_hand_side in prods:
        for unit_production in right_hand_side:
            for char in unit_production:
                if char==non_terminal_token:
                    following_str = unit_production[unit_production.index(char) + 1:]
                    if following_str=='':
                        if non_terminal==non_terminal_token:
                            continue
                        else:
                            follow_ = follow_ | follow(non_terminal)
                    else:
                        follow_2 = first(following_str)
                        if 'ε' in follow_2:
                            follow_ = follow_ | follow_2-{'ε'}
                            follow_ = follow_ | follow(non_terminal)
                        else:
                            follow_ = follow_ | follow_2
    return follow_


terminals = []
non_terminals = []
productions = []
productions_dict = {}

no_of_terminals=int(input("Enter Number of terminals: "))
print("Enter the terminals :")
for i in range(no_of_terminals):
    terminals.append(input(f"terminal No. {i+1} : "))

no_of_non_terminals=int(input("Enter no. of non terminals: "))
print("Enter the non terminals :")
for i in range(no_of_non_terminals):
    non_terminals.append(input(f"Enter Non terminal No.  {i+1} : "))

starting_symbol = input("Enter the starting symbol: ")

no_of_productions = int(input("Enter no of productions: "))
print("Enter the productions:")
for i in range(no_of_productions):
    productions.append(input(f"Enter production No {i+1} : "))
productions = [s.replace('@', 'ε') for s in productions]

for non_terminal in non_terminals:
    productions_dict[non_terminal] = []

for production in productions:
    nonterm_to_prod = production.split("->")
    list_of_productions = nonterm_to_prod[1].split("/")
    for unit_production in list_of_productions:
        productions_dict[nonterm_to_prod[0]].append(unit_production)

FIRST = {}
FOLLOW = {}

#Initialising dictionary of FIRST and FOLLOW for all non terminals
for non_terminal in non_terminals:
    FIRST[non_terminal] = set()

for non_terminal in non_terminals:
    FOLLOW[non_terminal] = set()

for non_terminal in non_terminals:
    FIRST[non_terminal] = FIRST[non_terminal] | first(non_terminal)

FOLLOW[starting_symbol] = FOLLOW[starting_symbol] | {'$'}
for non_terminal in non_terminals:
    FOLLOW[non_terminal] = FOLLOW[non_terminal] | follow(non_terminal)

print("{: ^20}{: ^20}{: ^20}".format('Non Terminals','First','Follow'))
for non_terminal in non_terminals:
    print("{: ^20}{: ^20}{: ^20}".format(non_terminal,str(FIRST[non_terminal]),str(FOLLOW[non_terminal])))