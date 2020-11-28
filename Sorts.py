def hexXOR(x,y):
    X=[0,0]
    Y=[0,0]
    H = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    B = [0]*16
    for i in range(16):
        B[i] = i
    for j in range(2):
        for i in range(16):
            if x[j] == H[i]:
                X[j] = B[i]
    for j in range(2):
        for i in range(16):
            if y[j] == H[i]:
                Y[j] = B[i]
    x_bin = X[0]*16 +X[1]
    y_bin = Y[0]*16 +Y[1]
    print(hex(x_bin^y_bin))


def binUpNumber(a):
    upsNumber = 0
    if a%2 != 0:
        upsNumber += 1
        a -= 1
    div = 2
    while a != 0:
        while div < a:
            div *= 2
        if div == a:
            a -= div
            upsNumber += 1
            div = 2
        else: #div > a
            div /= 2
            a -= div
            upsNumber += 1
            div = 2
    #print(upsNumber)
    return upsNumber


def knightsAndLiars():
    n = int(input())
    condemn = input().split()
    liarsKnightsCounter = [0, 0]
    pointer = 0  # how to distinguish никак - просто выбирай меньшее

    def switch(p):
        return 0 if p == 1 else 1

    for i in range(n):
        if condemn[i] == '1':
            liarsKnightsCounter[pointer] += 1
        else:  # condemn[i] == '0'
            pointer = switch(pointer)
            liarsKnightsCounter[pointer] += 1

    print(min(liarsKnightsCounter[1], liarsKnightsCounter[0]))


def HowMuch():
    price = int(input())
    delta = int(input())
    m = int(input())
    money = 0
    week = 0
    days = 0
    while week != m:
        money += price
        days += 1
        price += delta
        if days%7 == 0:
            week += 1
    print(money)


def isEmpty(a):
    return len(a) == 0


def rightBracketSequence(seq):
    a = []
    for brace in seq:
        if brace == '(':
            a.append(brace)
        else:
            if isEmpty(a):
                print('NO')
                return
            a.pop()
            right = ')'
            if right != brace:
                print('NO')
                return
    if isEmpty(a):
        print('YES')


def leftShift(A, j):
    tmp = A[j][0]
    for k in range(5-1):
        A[j][k] = A[j][k+1]
    A[j][4]=tmp
def hoarSort(a):
    if len(a) <= 1:
        return
    barrier = a[0]
    L=[]
    M=[]
    R=[]
    for x in a:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoarSort(L)
    hoarSort(R)
    k=0
    for x in L+M+R:
        a[k] =  x
        k += 1
def sortBackNumbers():
    n =int(input())
    numbers = input()
    A = [['0']*5 for i in range (n)]
    j = 0
    i = 4
    for x in numbers:
        if x == ' ':
            j += 1
            i = 4
        else:
            A[j][i] = x
            i -= 1

    for j in range (n):
        while A[j][0] == '0':
            leftShift(A,j)

    hoarSort(A)

    for j in range(n):
        if j != 0:
            print(' ', end='')
        for i in range(4, -1, -1):
            if A[j][i] == '0':
                continue
            print(A[j][i], end='')


def hoarSortKey(a,key):
    if len(a) <= 1:
        return
    barrier = a[0][key]
    L=[]
    M=[]
    R=[]
    for i in range(len(a)):
        if a[i][key] < barrier:
            L.append(a[i])
        elif a[i][key] == barrier:
            M.append(a[i])
        else:
            R.append(a[i])
    hoarSortKey(L,key)
    hoarSortKey(R, key)
    k=0
    for x in L+M+R:
        a[k] =  x
        k += 1

a =[[80, 1.79],[80, 1.71],[75, 2.05],[75, 1.78],[80,1.79],[69, 1.65],[85, 1.74],[89, 1.77],[85, 1.80],[85, 1.81]]

def doubleKeySort(a):
    hoarSortKey(a,0)
    #print(a)
    i = 0
    j = 0
    k = 0
    while j < len(a):
        while j != len(a) and a[i][0] == a[j][0]:
            j += 1
        b = a[i:j]
        hoarSortKey(b, 1)
        i = j
        for x in b:
            a[k] = x
            k += 1
    print(a)


