fib=[]
fib.append(0)
fib.append(1)

n1=fib[len(fib)-1]


i=0
while i < 100:
    n1 = fib[len(fib)-1]
    n2 = fib[len(fib)-2]
    i = n2+n1
    fib.append(i)

print(fib)