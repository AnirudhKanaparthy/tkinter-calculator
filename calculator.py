def isfloat(num):
    try:
        float(num)
        return True
    except:
        return False

def infixToPost(infix: str) -> str:
    precedence = {'^' : 3, '*' : 2, '/' : 2, '%' : 2, '+' : 1, '-' : 1, '#' : 0, '(' : 0}
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    stack = ['#']
    post  = ""

    expr = infix.split()
    i = 0
    symbol = expr[0]

    #----------------------#
    while True: 
        if symbol.isnumeric() or isfloat(symbol) or symbol.lower() in alpha:
            post += symbol + ' '

        elif symbol == ')':
            popped = stack.pop()
            while popped != '(':
                post += popped + ' '
                popped = stack.pop()

        elif precedence[symbol] > precedence[stack[-1]] or symbol == '(':
            stack.append(symbol)

        elif precedence[symbol] <= precedence[stack[-1]] :
            popped = stack.pop()
            post += popped + ' '
            continue

        i += 1
        if i > len(expr) - 1:
            break
        symbol = expr[i]
    #----------------------#

    while len(stack) != 1:
        popped = stack.pop()
        post += popped + ' '

    return post
##########################################################################


def evaluate(first, second, sym):
    if sym == '^':
        return first ** second
    if sym == '*':
        return first*second
    if sym == '/':
        return first/second
    if sym == '+':
        return first+second
    if sym == '-':
        return first-second
    if sym == '%':
        return first%second
##########################################################################


def calculate(expr: str) -> float:
    postfix = infixToPost(expr)
    postExpr = postfix.split()

    stack = list()
    for sym in postExpr:
        if sym.isnumeric() or isfloat(sym):
            stack.append(sym)
        else:
            second = float(stack.pop())
            first  = float(stack.pop())
            stack.append(evaluate(first, second, sym))
    return float(stack[-1])
##########################################################################  