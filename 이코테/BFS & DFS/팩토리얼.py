
def factorial_iterative(N):
    res=1
    for i in range(1, N+1):
        res*=i
    return res
fact = factorial_iterative(5)
print (fact)

def factorial_recursive(N):
    if N<=1:
        return
    return N*factorial_iterative(N-1)
print (factorial_recursive(5))