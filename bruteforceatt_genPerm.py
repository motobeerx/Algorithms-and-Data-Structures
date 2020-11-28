password = [9, 7, 't', 'g']
allow = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 't', 'g']
answer = []

def hackPassword(n:int, realPass, allow:list, prefix = None):

    """ n -nnumber of the max allowed digits
    realPass - real password
    allow - list of the available symbols in the password
    The function is supposed to hack realPass using Brute Force Method implemented via recursion """

    prefix = prefix or []
    if n == 0:
        if realPass == prefix:
            print(prefix, 'Hack it!')
            return
        print(prefix, 'Access Denied')
        return
    for x in allow:
        prefix.append(x)
        hackPassword(n-1, realPass, allow, prefix)
        prefix.pop()


hackPassword(4, password, allow)

