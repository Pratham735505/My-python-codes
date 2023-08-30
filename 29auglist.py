#to print the index of a character appearing in the list
'''
l = eval(input("Enter a list:"))
ch=eval(input('Enter character:'))
c=0
print("Index:",end='')
for i in range(len(l)):
    if l[i]==ch:
        print(i,end=' ')
        c+=1
print()
print(ch,"is",c,"times in the list")
'''

'''finding max and min in the list'''
'''
mx=0
mi=0
l = eval(input("Enter list:"))
for i in l:
    if mx<i:
        mx=i
print("Max element is:",mx)
mi=mx

for i in l:
    if mi>i:
        mi=i
print("Min element is:",mi)
'''

'''Wap to calculate the mean of list of numbers'''
'''
l=eval(input("Enter list:"))
s=0
for i in l:
    s=s+i
s=s/len(l)
print("The mean of elements of list",l,'is',s)'''


