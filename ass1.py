'''base=int(input("Enter base of parallelogram:"))
width=int(input("Enter width of parallelogram:"))
height=int(input("Enter height of parallelogram:"))
print("Area of parallelogram=",base * height)
print("Perimeter=",2*(base+width))


n=input("Enter name:")
id=int(input("Enter id:"))
p=(int(input("Enter marks of 5 subjects"))+int(input())+int(input())+int(input())+int(input()))/5
print(n,id,p)

a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))
print("Sum1=",a+b+c)
if a==b and b==c:
    print("Sum2:",0)
elif a==b:
    print("Sum2:",c)
elif a==c:
    print("Sum2:",b)
elif b==c:
    print("Sum2:",a)



n=int(input("Enter upto which you want the series to be printed:"))
c=1
s=0
while(n>0):
    f=0
    d=1
    e=0
    while e<c:
        f=f+d
        d+=1
        e=e+1
    s=s+f
    c=c+1
    n=n-1
print("The sum of series is=",s)

L=[]
for i in range(10):
    L.append(int(input("Enter number:")))
a=L[0]
count=0
for i in range(1,10):
    if a>L[i]:
        a=L[i]

print(a,"is the smallest")
L.remove(a)
a=L[0]
for i in range(1,9):
    if a>L[i]:
        a=L[i]
print(a,"is the 2nd smallest")

n=int(input("Enter a number:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)

bmi=eval(input("Enter weight in kg:"))/(eval(input("Enter height in meters:"))**2)
print("BMI of the person is:",bmi,"per kg meter square")

x=eval(input("Enter a number:"))
n=eval(input("Enter the power:"))
y=1
s=0
for i in range(n):
    s=s+(x**y)/y
    print(x,"**",y,"/",y,end="",sep='')
    if y<=n-1:
        print("+",end='',sep='')
    else:
        print("=",end='',sep='')
    y += 1
print(s)'''

'''a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
L=[a,b,c]
L.sort()
print(L[0],"is smallest")
print(L[1],"is 2nd smallest")
print(L[2],"is largest")

a=1
b=-4
for i in range(7):
    print(a,end=' ')
    a=a+6
    print(b,end=' ')
    b=b-6

s=1
n=int(input("Enter:"))
for i in range(2,n+1):
    if i**2%2==0:
        s=s+i**2
    else:
        s=s-i**2
print(s)

n=int(input())
s=0
d=0
for i in range(n):
    d=d*10+1
    s=s+d
print(s)

s=0
n=int(input("Enter number of terms:"))
d=4
a=3
for i in range(n):
    s=s+a
    if i!=n-1:
        print(a,"+",end='')
    else:
        print(a,"=",end='')

    a=a+d
    d+=2
print(s)
'''

'''n=int(input())
d=n-1
for i in range(n):
    for j in range(n):
        if j>=d:
            print("*",end='')
        else:
            print(' ',end='')

    d-=1
    print()

l=['A','B','C','D','E']
for i in range(len(l)):
    for k in range(len(l)-i-1):
        print(" ",end='')
    for j in range(2*i+1):
        if i%2==0:
            if j%2==0:
                print(l[i],end='')
            else:
                print(" ",end='')

        else:
            if j%2==0:
                print(l[i], end='')
            else:
                print(" ", end='')

    print()

n=int(input())
for i in range(n):
    for k in range(n-i-1):
        print(" ",end='')
    for j in range(2*i+1):
        if j%2==0:
            print(10,end='')
       # else:
       #     print(0,end='')
    print()'''


