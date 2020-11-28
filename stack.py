stack =[]
def push(x):
    stack.append(x)
def pop():
    x = stack.pop()
    return x
def isEmpty():
    return len(stack) == 0
def clear():
    stack.clear()


def checkBraceSequence(s:str):
    for brace in s:
        if brace not in '()[]/':
            continue
        if brace in '([/':
            stack.append(brace)
        else:
            assert brace in ')]/'
            if isEmpty():
                return False
            left = stack.pop()
            if left == '(':
                right = ')'
            if left == '[':
                right = ']'
            if left == '/':
                right = '/'
            if right != brace:
                return False
            return isEmpty()
def inputExpr():
    x=0
    expresion = []
    while True:
        x = input()
        if x == '#':
            break
        expresion.append(x) if x in '+-*/()' else expresion.append(int(x))
    return expresion

def shuntingYard():
    output =[]
    operators =[]
    expr = inputExpr()
    for x in expr:
        if type(x) is str:
            j = len(operators)
            if x in '+-*/':
                if x == '*':
                    id = 3
                elif x == '/':
                    id = 2
                elif x == '+':
                    id = 1
                else:  # x == '-':
                    id = 0
                if j == 0:
                    operators.append([x, id])
                    continue
                for i in range(j-1, -1, -1):
                    if i == 0:
                        if operators[i][1] > id:
                            k = operators.pop()
                            output.append(k[0])
                            operators.append([x, id])
                            break
                    if operators[i][1] > id:
                        k = operators.pop()
                        output.append(k[0])
                    else:
                        operators.append([x, id])
                        break
            elif x in '()':
                if x == '(':
                    id = -1
                    operators.append([x,id])
                else: # x == ')'
                   for i in range(j-1, -1, -1):
                       if operators[i][0] != '(':
                           k = operators.pop()
                           output.append(k[0])
                       elif operators[i][0] == '(':
                           operators.pop()
                       else:
                           pass

            else:
                pass
        else:
            output.append(x)

    while len(operators) != 0:
        x = operators.pop()
        output.append(x[0])
    print (output)
    return output


def stackCalculator():
    expr = shuntingYard()
    stack = []
    for k in expr:
        if (type(k) is int) or (type(k) is float):
            stack.append(k)
        else: #operation
            if k == '+':
                y=stack.pop()
                x=stack.pop()
                z = x + y
                stack.append(z)
            elif k == '-':
                y = stack.pop()
                x = stack.pop()
                z = x - y
                stack.append(z)
            elif k == '*':
                y = stack.pop()
                x = stack.pop()
                z = x * y
                stack.append(z)
            elif k == '/':
                y = stack.pop()
                x = stack.pop()
                z = x / y
                stack.append(z)
            else:
                print('Invalid Token')
                return
    print(stack.pop()) if len(stack) == 1 else print('Invalid Expression')

stackCalculator()