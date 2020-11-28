def genNumber(N: int, M: int, prefix=None):
    """ This function generates numbers with base N with the length of number M"""
    prefix = prefix or []
    if M==0:
        print(*prefix)  # print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        genNumber(N, M-1, prefix)
        prefix.pop()


def seek(number, prefix):
    for x in prefix:
        if number == x:
            return True
    return False


def genPermutations(N:int, M:int = -1, prefix=None):
    """ This function generates permutations for N numbers in M positions"""
    M = M if M != -1 else N
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for number in range(1, N+1):
        if seek(number, prefix):
            continue
        prefix.append(number)
        genPermutations(N, M-1, prefix)
        prefix.pop()

genPermutations(3)
