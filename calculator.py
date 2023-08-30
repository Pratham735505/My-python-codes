A=[]
B=[]
d=0
prob=input("Enter the problem:")
for i in prob:
    if ord(i)>=48 and ord(i)<=57:
        A.append(int(i))

    else:
        B.append(i)
for j in range(len(A)-1):
    if B[j]=='+':
        d=d+A[j]+A[j+1]
    elif B[j]=='-':
        d=d+A[j]-A[j+1]
    elif B[j]=='*':
        d=d+A[j]*A[j+1]
    elif B[j]=='/':
        d=d+A[j]/A[j+1]
    elif B[j]=='%':
        d=d+A[j]%A[j+1]
    elif B[j]=='-':
        d=d+A[j]-A[j+1]
print(d)