#To check if each number in list is prime or not
'''
l=eval(input("Enter list:"))
f=0
for i in l:
    n = i
    g = 0
    while (n > 0):
        if i % n == 0:
            g += 1
        n = n - 1
    if g != 2:
        f=1
        break
if f==0:
    print(True)
else:
    print(False)
'''

#convert list elements into single data type
'''
l=eval(input("Enter list:"))
s=''
for i in l:
    s+=str(i)
print(s)
'''

#take a nested list and find out list whose elements sum is highest
'''
l=eval(input("Enter list:"))
h=None
m=0
s=0
for i in l:
    if type(i)==list:
        s=0
        for j in i:
            s=s+j
        if s>m:
            m=s
            h=i
print("list is:",h,"Sum of its element is:",m)
'''

#program to pack consecutive duplicates of a given list of element into sublists
'''
l=eval(input("Enter list:"))
n=[]
d=[]
d.append(l[0])
for i in range(1,len(l)):
    if l[i - 1] == l[i]:
        d.append(l[i])
    else:
        n = n + [d]
        d = []
        d.append(l[i])
n=n+[d]
for i in n:
    print(i)
'''