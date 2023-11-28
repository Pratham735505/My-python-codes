e=0
g=0
for i in range(1,99):
    g=0
    e=0
    n=i
    print('check')
    while (n > 0):
        if i % n == 0:
            g += 1
            n = n - 1
    if g==2:
        print(i)
    n = i+2
    while (n > 0):
        if (i+2) % n == 0:
            e += 1
            n = n - 1
    if e==2 and g==2:
        print(i,i+2)