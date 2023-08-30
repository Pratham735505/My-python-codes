'''import math
m = int(input("Enter lower limit:"))
n = int(input("Enter upper limit:"))
c = int(input("1.Prime Number\n2.Armstrong Number\nEnter choice:"))
for i in range(m,n+1):
    if c==1:
        n = i
        g = 0
        while (n > 0):
            if i % n == 0:
                g += 1
            n = n - 1
        if g == 2:
            print(i, "is prime")
    elif c==2:
        n=str(i)
        l=len(n)
        i=int(n)
        n=i
        s=0
        while n>0:
            s=s+math.pow(n%10,l)
            n=n//10
        if s==i:
            print(i)

    else:
        print("Invalid choice")

'''

'''
n=int(input("Enter upper limit:"))
m=int(input("Enter dividend:"))

for i in range(1,n+1):
    if i%m==0:
        if i%2==0:
            print(i,"is divisible by",m,"and",i,"is even")
        else:
            print(i,"is divisible by", m, "and", i, "is odd")

'''
'''
d=1
n=int(input("Enter final value:"))
for i in range(1,n+1):
    l=i
    s=1
    while l>=1:
       s=s*l
       l-=1
    print(s)
    d=d+1/s
print(d)
'''
'''
n=int(input("Enter upto which series to be printed:"))
for i in range(n+1):
    for j in range(65,65+i):
        print(chr(j),end='')
    print()
'''
'''

n=int(input("Enter :"))
for i in range(n):
    for k in range(n - i - 1):
        print(" ", end='')
    for j in range(2*i+1):
        print("*",end='')
    print()
for i in range(n):
    for k in range(i):
        print(" ", end='')
    if i!=0:
        for j in range(2 * (n - i) - 1):
            print("*", end='')
        print()

'''

n=int(input("Enter :"))
for i in range(n):
    for k in range(n - i - 1):
        print(" ", end='')
    for j in range(2*i+1):
        if j==0 or j==2*i:
            print("*",end='')
        else:
            print(" ",end='')
    print()
for i in range(n):
    for k in range(i):
        print(" ", end='')
    if i!=0:
        for j in range(2 * (n - i) - 1):
            if j==0 or j==2*(n-i)-2:
                print("*", end='')
            else:
                print(" ", end='')
        print()

