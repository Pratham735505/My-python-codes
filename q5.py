n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
lcm=0
i=1
if n1==n2:
    lcm=n1
else:
    if n1>n2:
        while True:
            if (n1*i)%n2==0:
                lcm=n1*i
                break
            i=i+1
    else:
        while True:
            if (n2*i)%n1==0:
                lcm=n2*i
                break
            i=i+1
gcd=(n1*n2)/lcm

print("LCM and GCD are:",lcm,gcd)