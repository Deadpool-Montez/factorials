#w/o Recursion

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        a, b = b, a+b

fibonacci(20)

#with Recursion

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print (fibonacci(i))