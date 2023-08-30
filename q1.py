b=0
l=[]
for i in range(10):
    n=int(input("Enter number:"))
    l.append(n)
a=l[0]
for j in l:
    if j==0:
        a=j
    if a>j:
        a=j
if l[0]==a:
    b=l[1]
else:
    b=l[0] 
for j in l:
    if b>j and b!=a:
        b=j
print("Lowest:",a)
print("Second lowest:",b)