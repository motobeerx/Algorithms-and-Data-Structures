def merge(A:list, B:list):
    C = [0]*(len(A)+len(B))
    i=k=m=0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[m] = A[i]
            i += 1
            m += 1
        else:
            C[m] = B[k]
            k += 1
            m +=1
    while i < len(A):
        C[m] = A[i]
        i += 1
        m += 1
    while k < len(B):
        C[m] = B[k]
        k += 1
        m += 1
    return C

def mergeSort(A):
    if len(A) <= 1:
        return
    mid = len(A)//2
    L = [A[i] for i in range(0, mid)]
    R = [A[i] for i in range(mid, len(A))]
    mergeSort(L)
    mergeSort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


def hoarSort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L=[]
    R=[]
    M=[]
    for x in A:
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
        A[k] = x
        k += 1

def checkSort(A,asc = True):
    s =2*int(asc) - 1
    for i in range(len(A) - 1):
        if s*A[i] > s*A[i+1]:
            return False
    return True



A = [4,3,2,5,2,2,1,6,7,8,4,5,3,7,8,9,1,2,3,4,2,5,6,7,8]
mergeSort(A)
print(A)

B = [4,3,2,5,2,2,1,6,7,8,4,5,3,7,8,9,1,2,3,4,2,5,6,7,8]
hoarSort(B)
print(B)
