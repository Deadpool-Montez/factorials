#with recursion
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

#using addition
def sum(n):
    if n==1 or n==0:
        return n
    else:
        return n + sum(n-1)
print(sum(0))