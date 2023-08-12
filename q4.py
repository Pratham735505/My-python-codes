l=[]
b=[]
for i in range(2,12):
    l.append(2**i-1)
print("First 10 mersenne numbers are:",l)
for j in l:
    a=j
    g=0
    while a>0:
        if j%a==0:
            g+=1
        a=a-1
    if g==2:
        b.append(j)
print("Prime mersenne are:",b)
