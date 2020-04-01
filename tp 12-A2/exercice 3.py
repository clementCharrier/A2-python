def pow(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    else :
        return x*pow(x,n-1)

print(pow(42,3))
