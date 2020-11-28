def insert_sort(a):
    for top in range(1,len(a)):
        k = top
        while k>0 and a[k-1]>a[k]:
            a[k], a[k-1] = a[k-1], a[k]
            k -= 1


def choise_sort(a):
    for pos in range(0, len(a)-1):
        for k in range(pos+1,len(a)):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]


def bubble_sort(a):
    for bypass in range(1, len(a)):
        for k in range(0, len(a) - bypass):
            if a[k] > a[k+1]:
               a[k], a[k+1] = a[k+1], a[k]


def count_sort(a):
    f = [0]*10
    dig = range(10)
    for k in range(len(a)):
        if a[k] == dig[a[k]]:
            f[a[k]] += 1
    b = [0]*len(a)
    pos = 0
    while pos < len(a):
        for digit in range(len(f)):
            for x in range(f[digit]):
                b[pos] = digit
                pos += 1
    return b


def sort_test(insert_method):
    a = [8,7,5,9,8,2,7,1,9,4,3,9,6,2,9,8]
    insert_method(a)
    a1 = [1,2,2,3,4,5,6,7,7,8,8,8,9,9,9,9]
    print('test case #1 OK' if a == a1 else 'test case #1 FAIL')
    print(a)

    
def sort_test2(insert_method):
    a = [8,7,5,9,8,2,7,1,9,4,3,9,6,2,9,8]
    print(a)
    print(insert_method(a))


sort_test(insert_sort)
sort_test(choise_sort)
sort_test(bubble_sort)
sort_test2(count_sort)