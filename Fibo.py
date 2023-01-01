a=0
b=1
c=1
n=int(input("Enter upto fibonacci series is to be printed="))
if n<0:
    print("Wrong entry")
elif n==0:
   
    print(a)
elif n==1:
    print(b)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(0,n):
        a=b
        b=c
        c=a+b
        print(c)
