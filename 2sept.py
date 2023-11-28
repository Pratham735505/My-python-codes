#entering a sentence and reversing every word
'''
s=input("Enter a sentence:")
s2=''
g=''
c=0
for i in range(len(s)):
    if ord(s[i])==32:
        g=s[c:i]
        s2=s2+' '+ g[::-1]
        c=i+1
    elif i==len(s)-1:
        g=s[c:len(s)]
        s2 = s2 + ' ' + g[::-1]
print(s2)
'''

#changing name and age in sentence
'''
s='My name is Abc and my age is 45'
n=input('Enter right name:')
age=int(input('Enter age:'))
i=0
v=''
while i<(len(s)):
    if s[i:i+3]=='Abc':
        v=v+' '+n
        i+=2
    elif s[i:i+2]=='45':
        v=v+' '+str(age)
        i=i+1
    else:
        v=v+s[i]
    i+=1
print(v)
'''
#togglecase
'''
s=input('Enter string:')
g=''
for i in range(len(s)):
    if i%2==0:
        if ord(s[i])>=65 and ord(s[i])<=97:
            g=g+chr(ord(s[i])+32)
        else:
            g=g+s[i]
    else:
        if ord(s[i])>=98 and ord(s[i])<=129:
            g=g+chr(ord(s[i])-32)
        else:
            g=g+s[i]
print(g)
'''
'''
s=input("Enter a sentence:")
s2=''
g=''
c=0
for i in range(len(s)):
    if ord(s[i])==32:
        g=s[c:i]
        if g=='Blue':
            s2=s2+' '+'Red'
        elif g == 'blue':
            s2 = s2 + ' ' + 'red'
        else:
            s2=s2+' '+ g
        c=i+1
    elif i==len(s)-1:
        g=s[c:len(s)]
        if g=='Blue':
            s2=s2+' '+'Red'
        elif g == 'blue':
            s2 = s2 + ' ' + 'red'
        else:
            s2=s2+' '+ g
print(s2)
'''
#accept a sentence and delete repeated words
'''
s=input("Enter a sentence:")
g=''
i=0
while i<len(s):
    if s[i]==s[i-1]:
        pass
    else:
        g=g+s[i]
    i+=1
print(g)'''


#unique string
'''
s=input("Enter string:")
g=''
d=0
for i in s:
    if i in g:
        d=1
        break
    g=g+i
if d==1:
    print('Not unique string')
else:
    print('Unique string')
'''

s=input('Enter string:')
s=s+s[::-1]
print(s)