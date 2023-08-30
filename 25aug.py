'''
s = input("Enter string:")
st = input("Enter sub-string:")
l=len(st)
count=0
for i in range(len(s)):
    if st[0]==s[i]:
        flag=0
        e=1
        g=i+1
        while e<l:
            if g>=len(s):
                break
            if st[e]==s[g]:
                pass
            else:
                flag=1
                break
            e+=1
        if flag==0:
            count+=1
print(st,"is",count,"times")
'''
'''
s = input("Enter a message:")
ch = int(input("1.Encrypt\n2.Decrypt\nEnter choice:"))
if ch==1:
    s1=''
    for i in s:
        e=chr(ord(i)+1)
        s1=s1+e
    print("Encrypted string:", s1)
elif ch==2:
    s1 = ''
    for i in s:
        e = chr(ord(i) - 1)
        s1 = s1 + e
    print("Decrypted string:",s1)

else:
    print("Wrong choice")
'''

'''Email Validation'''

'''
e = input("Enter Email:")
c = '@gmail.com'
i=0
f=0
while i<len(e):
    if e[0]==c[0]:
        f=1
        break
    if e[i]==c[0]:
        break
    i+=1
if e[i:]==c and f==0:
    print(e,"is invalid")
else:
    print(e,'is invalid')
'''
'''Wap to capitalize the first letter of each word in string'''
'''
s = input("Enter a string:")
n = ord(s[0])
if n>=97:
    n = n-32
    n = chr(n)
for i in (1,len(s)-1):
    if ord(s[i-1]) ==32 and ord(s[i]) !=32:
        if ord(s[i])>=97:
            print(i)
            n=n+ chr(ord(s[i])-32)
        else:
            n = n + s[i]
    else:
        n=n+s[i]
print(n)'''

'''s = input("Enter a string:")
g=''
for i in range(len(s)):
    if i%2==0:
        g = g + s[i]
print(g)
'''


'''
s = input("Enter a string:")
l=''
for i in range(len(s)-1,-1,-1):
    l=l+s[i]
print(l)
'''
'''
s = input("Enter a string:")
l=''

for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[j] not in l:
            if s[i]==s[j]:
                c+=1
    if c==1:
        l=l+s[i]

print("The non repeating characters are:")
for i in l:
    print(i)
'''

'''
s = input("Enter a string:")
l=''
m=[]
for i in range(len(s)):
    if ord(s[i])==32:
        m.append(l)
        l=''
    elif i==len(s)-1:
        l=l+s[i]
        m.append(l)
    else:
        l=l+s[i]
g=''
print(m)
for i in m:
    g = g + i[len(i)::-1]+' '

print(g)
'''

'''
l=''
    if ord(s[i])==32:
        j=i+1
        while ord(s[j])!=32 and s[j]!=len(s)-1:
            #print(j)
            j+=1
        l=l+s[i:j+1]
    if l!='':
        print(l)
'''



'''
s= input("Enter string:")
l=[]
for i in s:
    l.append(i)
for j in range(len(l)):
    for i in range(len(l)-1):
        if ord(l[i])>ord(l[i+1]):
            l[i],l[i+1]=l[i+1],l[i]
s=''
for i in l:
    s=s+i
print(s)
'''
'''
#Program to print non repeating characters in a string
s = input("Enter string:")
g=''
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i]==s[j]:
            c+=1
    if c==1:
        g=g+s[i]
print(g)
'''
'''
#removing whitespaces and commas
s= input("Enter string:")
l=''
for i in range(len(s)):
    if s[i]!=',' and ord(s[i])!=32:
        l=l+s[i]
print(l)
'''


'''
#counting each character
s = input("Enter string:")
g=''
l=''
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if s[i] not in l:
            if s[i]==s[j]:
                c+=1
    if s[i] not in l:
        print(s[i],'is',c,'times')
    l=l+s[i]
'''

a=input("Enter string 1:")
b=input("Enter string 2:")
count=0
c=0
for i in a:
    for j in b:
        if i==j:
            count=count+1
            if count==len(a):
                print("Strings are anagram of each other.")
                c=1
if count!=len(a) and c==0:
    print('Strings are not anagram of each other')