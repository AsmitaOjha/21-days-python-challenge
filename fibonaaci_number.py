n = int(input("The term upto which fibonacci number is needed: "))
fib1=0
fib2=1
i=3
while(i<=n):
    fib = fib1 + fib2
    fib1=fib2
    fib2=fib
    i=i+1
    print(fib)