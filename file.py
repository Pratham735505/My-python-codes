# Create a file student that stores the details of the studens
'''
file = open('student.txt','w')
file.writelines(['Id','Name','CGPA','Course'])
while True:
    id=int(input('Enter Id:'))
    name = input('Enter Name:')
    cg=float (input('Enter CGPA:'))
    course = input('Enter course:')
    l=[str(id),name,str(cg),course]
    file.writelines(l)
    c=input('Do you want to enter more?Y/N:')
    if c=='Y' or c=='y':
        continue
    else:
        break
file.close()
'''

#Create a function in python that accepts a filename and reports the files longest line
'''
n = input('Enter name of the file:')
file = open(n,'r')
s = ''
y=file.readline()
while y!='':
    if len(y)>len(s):
        s=y
    y=file.readline()
print(s)
file.close()
'''

#A text file is created that contains alphanumeric text.. Now read that text file and print only digits from that file
'''
file = open('read.txt','r')
c = file.read()
for i in c:
    if ord(i)>=48 and ord(i)<=57:
        print(i,end='')
file.close()

'''

#Wap that copies a text file a text file src.txt onto target.txt barring lines having special symbols @,.,?
'''
file1 = open('src.txt','r')
file2 = open('target.txt','w')
s = file1.readline()
while s!='':
    if '@' not in s and '.' not in s and '?' not in s:
        file2.write(s)
    s=file1.readline()
file2.close()
file1.close()
'''

# WAP to create a file having a list of telephone numbers stored with the names. Write a function to count the names. Write a function to count the telephone
# numbers of all the customers whose name, starts with A or M and ends with N or H
'''
file = open('telephone.txt','r')
g = file.readline()
count = 0
while g!='':
    d =  g.split()
    if (d[0][0]=='A' or d[0][0]=='a' or d[0][0]=='M' or d[0][0]=='m') and (d[0][-1]=='N' or d[0][-1]=='n' or d[0][-1]=='H' or d[0][-1]=='h'):
        if d[1].isdigit():
            count+=1
    g = file.readline()
print(count)

file.close()
'''

#q1 menu drive code for adding, updating a record, deleting a record


while True:
    c = int(input('1.Add new record\n2.Delete Record\n3.Update Existing Record\n4.Display all records\n5.Display top 5 record\nEnter choice:'))
    if c == 1:
        file = open('record.txt', 'a+')
        id = str(int(input('Enter student id:')))
        n = input('Enter name:')
        contact = str(int(input('Enter contact:')))
        per = str(float(input('Enter percentage:')))
        file.writelines([id,' ', n,' ', contact,' ', per])
        print('File stored successfully')
        file.close()
    elif c == 2:
        # error
        file = open('record.txt', 'a+')
        id = str(int(input('Enter id of the student whose record you want to delete:')))
        g = file.readline()
        print(g) # error
        f=0
        while g!='':
            g=g.split()
            print(g)
            if id in g:
                g=[' '*len(g[0]),' ',' '*len(g[1]),' ',' '*len(g[2]),' ',' '*len(g[3])]
                f = 1
                break
            g=file.readline()
        file.close()
        if f == 0:
            print('Record not found')
        else:
            file=open('record.txt')
            file.writelines(g)
            print('Record Deleted')
            file.close()

    elif c == 3:
        file = open('record.txt', 'a+')
        id = str(int(input('Enter id of the student whose record you want to delete:')))
        g = file.readline()  # error
        f = 0
        for i in g:
            if id in i:
                p = i.split()
                d = int(input(''))
                f = 1
                break
        file.close()
        if f == 0:
            print('Record not found')
        else:
            file=open('record.txt')
            file.writelines(g)
            print('Record Updated')
            file.close()
    elif c == 4:
        file=open('record.txt','a+')
        g = file.readline()
        while g != '':
            d = g.split()
            print(d)
            g = file.readline()
        file.close()
    elif c == 5:
        file=open('record.txt','a+')
        print('Top 5 records are:')
        file.seek(0)
        g = file.readline()
        l = []
        while g != '':
            l.append(g)
            g = file.readline()
        for i in range(len(l)):
            for j in range(len(l) - 1):
                if l[j][3] < l[j + 1][3]:
                    l[j], l[j + 1] = l[j], l[j + 1]
        if len(l) < 5:
            for i in range(len(l)):
                print(l[i])
        else:
            for i in range(5):
                print(l[i])
        file.close()
    else:
        print('Invalid Choice')
    ch = input('Do you want to run again Y/N?')
    if ch=='y' or ch=='Y':
        continue
    else:
        break

