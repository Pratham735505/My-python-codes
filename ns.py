name=input("Enter name of employee:")
g=input("Enter Grade:")
if g=='a' or g=='A':
    sal=eval(input("Enter the basic salary 35000-40000 :"))
    TA=0.7*sal
    DA=0.8*sal
    PF=0.3*sal
    NS=(sal+DA+TA)-PF


elif g=='b' or g=='B':
    sal=eval(input("Enter the basic salary 25000-35000 :"))
    TA=0.5*sal
    DA=0.6*sal
    PF=0.7*sal
    NS=(sal+DA+TA)-PF

elif g=='c' or g=='C':
    sal=eval(input("Enter the basic salary 15000-25000 :"))
    TA=0.35*sal
    DA=0.45*sal
    PF=0.1*sal
    NS=(sal+DA+TA)-PF

elif g=='d' or g=='D':
    sal=eval(input("Enter the basic salary 10000-15000 :"))
    TA=0.2*sal
    NS=TA+sal
else:
    print("Invalid Grade")
print("Name :",name)
print("Net Salary is:",NS)
