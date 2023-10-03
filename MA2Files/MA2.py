"""
Solutions to module 2 - A calculator
Student: Carl Agelii
Mail: calle.ageli01@gmail.com
Reviewed by: Jens
Reviewed date: 2023-09-18
"""

"""
Note:
The program is only working for a very tiny set of operations.
You have to add and/or modify code in ALL functions as well as add some new functions.
Use the syntax charts when you write the functions!
However, the class SyntaxError is complete as well as handling in main
of SyntaxError and TokenError.
"""

import math
from tokenize import TokenError  
from MA2tokenizer import TokenizeWrapper


class SyntaxError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)

class EvaluationError(Exception):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(self.arg)       

def log(x):
    if x<=0:
        raise EvaluationError(f"Argument to log is {x}. Must be >= 0")
    else:
        return math.log(x)
    
def fib(n):
    if float(n).is_integer() == False or n <= 0:
        raise EvaluationError(f"Argument to fib is {n}. Must be integer >= 0")
    
    memory = {0: 0, 1: 1}

    def _fib(n):
        if n not in memory:
            memory[n] = _fib(n-1) + _fib(n-2)
        return memory[n]

    return _fib(n)

def fac(n):
    """ Computes and returns n!"""
    if float(n).is_integer() == False or n < 0:
        raise EvaluationError(f"Argument to fac is {n}. Must be integer >= 0")
    if n == 0:
        return 1
    else:
        return int(n*fac(n-1))


def mean(values):
    return sum(values)/len(values)

functions_1 = {"sin" : math.sin, "cos" : math.cos, "exp" : math.exp, "log" : log, "fac": fac, "fib" : fib, "abs": abs}
functions_n = {"sum" : sum, "max" : max, "min" : min, "mean" : mean}

def arglist(wtok, variables):
    result = []
    if wtok.get_current() != '(':
        raise SyntaxError('Expected (')
    while True:
        wtok.next()
        result.append(assignment(wtok, variables))
        if wtok.get_current() == ')':
            return result
        elif wtok.get_current() != ',':
            raise SyntaxError('Expected , or ) in function')


def statement(wtok, variables):
    """ See syntax chart for statement"""
    result = assignment(wtok, variables)

    if wtok.is_at_end():
        return result
    else:
        raise SyntaxError('Unexpected token')
    

    
def assignment(wtok, variables):
    """ See syntax chart for assignment"""
    result = expression(wtok, variables)
    while True:
        if wtok.get_current() == '=':
            wtok.next()
            if wtok.is_name():
                variables.update({wtok.get_current(): result})
                wtok.next()
            else:
                raise SyntaxError('Expected variable name after =')
        else:
            return result

    

def expression(wtok, variables):
    """ See syntax chart for expression"""
    result = term(wtok, variables)
    while True:
        if wtok.get_current() == '+':
            wtok.next()
            result = result + term(wtok, variables)
        elif wtok.get_current() == '-':
            wtok.next()
            result = result - term(wtok, variables)
        else:
            return result
    


def term(wtok, variables):
    """ See syntax chart for term"""
    result = factor(wtok, variables)
    while True:
        if wtok.get_current() == '*':
            wtok.next()
            result = result * factor(wtok, variables)
        elif wtok.get_current() == '/':
            wtok.next()
            try:
                result = result / factor(wtok, variables)
            except:
                raise EvaluationError('Division by zero')
        else:
            return result
    


def factor(wtok, variables):
    """ See syntax chart for factor"""
    if wtok.get_current() == '(':
        wtok.next()
        result = assignment(wtok, variables)
        if wtok.get_current() != ')':
            raise SyntaxError("Expected ')'")
        else:
            wtok.next()
    
    elif wtok.get_current() in functions_1:
        func = wtok.get_current()
        wtok.next()
        if wtok.get_current() == '(':
            wtok.next()
            result = functions_1[func](assignment(wtok,variables))
            wtok.next()
            return result
        else:
            raise SyntaxError(f'Expected ( after {func}')


    elif wtok.get_current() in functions_n:
        func = wtok.get_current()
        wtok.next()
        result = functions_n[func](arglist(wtok,variables))
        wtok.next()
        return result

    elif wtok.get_current() in variables:
        result = variables[wtok.get_current()]
        wtok.next()
        return result

            
    elif wtok.is_number():
        result = float(wtok.get_current())
        wtok.next()
        return result

    elif wtok.get_current() == '-':
        wtok.next()
        result = -1*factor(wtok,variables)
        return result
    
    elif wtok.is_name():
        raise EvaluationError(f'Unknown variable {wtok.get_current()}')

    else:
        raise SyntaxError(
            "Expected number, variable or '('")  
    return result


         
def main():
    """
    Handles:
       the iteration over input lines,
       commands like 'quit' and 'vars' and
       raised exceptions.
    Starts with reading the init file
    """
    
    print("Numerical calculator")
    variables = {"ans": 0.0, "E": math.e, "PI": math.pi}
    
    
    # Note: The unit test file iniiate variables in this tway. If your implementation 
    # requires another initiation you have to update the test file accordingly.
    init_file = 'MA2init.txt'
    lines_from_file = ''
    try:
        with open(init_file, 'r') as file:
            lines_from_file = file.readlines()
    except FileNotFoundError:
        pass

    while True:
        if lines_from_file:
            line = lines_from_file.pop(0).strip()
            print('init  :', line)
        else:
            line = input('\nInput : ')
        if line == '' or line[0]=='#':
            continue
        wtok = TokenizeWrapper(line)

        if wtok.get_current() == 'quit':
            print('Bye')
            exit()
        elif wtok.get_current() == 'vars':
            for key,value in variables.items():
                print(f'{key}\t : {value}')

            pass
        else:
            try:
                result = statement(wtok, variables)
                variables['ans'] = result
                print('Result:', result)

            except SyntaxError as se:
                print("*** Syntax error: ", se)
                print(
                f"Error occurred at '{wtok.get_current()}' just after '{wtok.get_previous()}'")
            
            except EvaluationError as ee:
                print("*** Evalutation error: ", ee)

            except TokenError as te:
                print('*** Syntax error: Unbalanced parentheses')
 


if __name__ == "__main__":
    main()