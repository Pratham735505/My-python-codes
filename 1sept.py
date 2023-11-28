#q1 to find the frequencies of all elements and tell unique or not
'''
l = eval(input("Enter a list:"))
f = 0
s=''
for i in range(len(l)):
    f=0
    for j in range(len(l)):
        if str(l[i]) not in s:
            if l[i]==l[j]:
                f+=1
    s=s+str(l[i])
    if f==1:
        print(l[i],"Unique element",f)
    elif f>1:
        print(l[i],"Duplicate element",f)
'''

#Q2 WAP to find the second largest number from a list of numbers
'''
l = eval(input("Enter a list:"))
m = 0
m2 =0

for i in l:
    if m<i:
        m=i
for i in l:
    if m2<i and i<m:
        m2=i
print("2nd largest number is:",m2)
'''

#Wap that inputs a list of numbers and shifts all zeroes to the right and non zeroes numbers to the left non-zeroes numbers to the left of the list
'''
l = eval(input("Enter list:"))
l2=[]
for i in l:
    if i==0:
        l2=l2+[i]
    else:
        l2=[i]+l2
print(l2)
'''

#wap for circular right shift of elements
l = eval(input("Enter list:"))
e=0
for i in range(len(l)):
    if i==0:
        e=l[(i+1)%len(l)]
        l[(i+1)%len(l)]=l[i]
    else:
        l[(i + 1) % len(l)],e=e,l[(i+1)%len(l)]
print(l)


#ask the user to enter a list of string and create a new list that consist of the stringer with their first characters removed
'''
l = eval(input("Enter list of string:"))
l2=[]
for i in range(len(l)):
   l2=l2+[0]
j=0
for i in l:
    l2[j]=i[1:len(i)-1]
    j+=1
print(l2)'''