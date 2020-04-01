def listSum(l):
    k=l[-1]
    l.pop()
    if len(l)==0:
        return k
    else :
        return k+listSum(l)


print(listSum([1,2,3,6]))
