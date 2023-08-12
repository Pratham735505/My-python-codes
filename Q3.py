n=int(input("Enter a number which is greater than 1000:"))
if n>1000:
    c=int(input("1.Palindrome Check\n2.Prime Check\nEnter Choice:"))
    if c==1:
        b=n
        s=0
        while b>0:
            d=b%10
            s=s*10+d
            b=b//10
        if s==n:
            print("Number is palindrome")
        else:
            print('Not palindrome')
    elif c==2:
        a=n
        g=0
        while(a>0):
            if n%a==0:
                g+=1
            a=a-1
        if g==2:
            print(n,"is prime")
        else:
            print(n,"is not prime")
    else:
        print("Invalid Choice")
else:
    print("Invalid entry")