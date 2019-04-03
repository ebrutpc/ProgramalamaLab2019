def fibonnaci_loop(n):
    a,b=0,1
    for i in range(n-1):
        a,b=b,a+b
    return a
sonuc=fibonnaci_loop(5)
print(sonuc)

def fibonacci_recursive(n):
    if(n<=3):
        return 1
    else:
        return fibonacci_recursive(n-1)+fibonacci_recursive(n-2)

result=fibonacci_recursive(5)
print(result)

def factorial_recursive(n):
    if(n==1):
        return 1
    else:
        return n*factorial_recursive(n-1)

result=factorial_recursive(5)
print(result)

def loop_factorial(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s

result=loop_factorial(5)
print(result)


def power_recursive(m,n):
    if(n==0):
        return 1
    elif(n==1):
        return m
    elif(n%2==0):
        return power_recursive(m*m,n//2)
    elif(n%2!=0):
        return power_recursive(m*m,n//2)*m

result=power_recursive(2,5)
print(result)

def loop_power(m,n):
    s=1
    for i in range(n):
        s=s*m
    return s
result=loop_power(2,5)
print(result)
