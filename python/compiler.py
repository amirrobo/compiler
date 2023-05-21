# Compiler (Tokenizer(Scanner) and Parser)
#regular expression library (search pattern)
import re

#Tokenizer function receives starting input
def tokenizer(input_expression):
    #counter variable for iterating through input array 
    current = 0
    #array to store computed tokens
    tokens = []
    #Use regex library to create search patterns for
    #letters a,z
    alphabet = re.compile(r"[a-z]", re.I);
    #numbers 1-9
    numbers = re.compile(r"[0-9]");
    #white space
    whiteSpace = re.compile(r"\s");
    #iterate through input
    while current < len(input_expression):
        #track position
        char = input_expression[current]
        #If white space is detected, no token created
        if re.match(whiteSpace, char):
            current = current+1
            continue
        #create + add token to array for open parens
        if char == '(':
            tokens.append({
                'type': 'left_paren',
                'value': '('
            })
            #continue iterating
            current = current+1
            continue
        #create + add token to array for closed parens
        if char == ')':
            tokens.append({
                'type': 'right_paren',
                'value': ')'
            })
            #continue iterating
            current = current+1
            continue
        #create + add token to array for numbers
        if re.match(numbers, char):
            value = ''
            #nested iteration if a number is multi-num 
            while re.match(numbers, char):
                value += char
                current = current+1
                char = input_expression[current];
            tokens.append({
                'type': 'number',
                'value': value
            })
            continue
        #create + add token to array for letters
        if re.match(alphabet, char):
            value = ''
            #nested iteration if a word is multi-char (all are in this case)
            while re.match(alphabet, char):
                value += char
                current = current+1
                char = input_expression[current]
            tokens.append({
                'type': 'name',
                'value': value
            })
            continue
        #error condition if we find an unknown value in the input
        raise ValueError('what are THOSE?: ' + char);
    return tokens

#The parse function creates an Abstract Syntax Tree given the computed
#tokens from the previous function   
def parser(tokens):
    #keep track of position while iterating
    global current
    current = 0
    #nested walk function for building an abstract syntax tree
    def walk():
        #keep track of position while iterating? 
        global current
        token = tokens[current]
        #if a number is encountered, return a "NumberLiteral" node
        if token.get('type') == 'number':
            current = current + 1
            return {
                'type': 'NumberLiteral',
                'value': token.get('value')
            }
          
        #if open parentheses encountered, return a "CallExpression" node
        if token.get('type') == 'left_paren':
           #skip past the parenthesis, we're not storing that
            current = current + 1
            token = tokens[current]
            #store the name of operation
            node = {
                'type': 'CallExpression',
                'name': token.get('value'),
                'params': []
            }
            #and this node will have child nodes as parameters
            #and input expression can have many nested expressions
            #so we'll use recursion to build a tree of relations!
            current = current + 1
            token = tokens[current]
            #until the expression ends with a closed parens
            while token.get('type') != 'right_paren':
                #recursively add nodes to the params array via the walk function
                node['params'].append(walk());
                token = tokens[current]
            current = current + 1
            return node
        #error if unknown type encountered
        raise TypeError(token.get('type'))
    
    
    #Let's initialize an empty Abstract Syntax Tree
    ast = {
        'type': 'Program',
        'body': []
    }
    #then populate it by calling the walk function
    #until the global current variable reaches the end of the token array
    while current < len(tokens):
        ast['body'].append(walk())
    #return the completed AST
    return ast

def compiler(input_expression):
    #given an input expression, create a set of tokens
    tokens = tokenizer(input_expression)
    #create an abstract syntax tree given those tokens
    ast    = parser(tokens)
    #return!
    # print(ast)
    return ast

def main():
    #test 
    input = "(add 2 (subtract 4 2))"
    output = compiler(input)
    print(output)

if __name__ == "__main__":
    main()