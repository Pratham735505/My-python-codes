l=[]
while True:
    for i in range(4):
        l.append([input('Element name:'),input('Enter symbol:'),int(input('Enter atomic number:')),int(input('Enter row:')),int(input('Enter column:')),input('Enter property:')])
    if input('Do you want to enter more(Y/N)?:')=='Y':
        continue
    else:
        break
print(l)
while True:
    n = int(input(
        '1.Collect info by entering element symbol\n2.Enter property\n3.All elements sorted by Atomic number\n4.Find element by row\n5.Find element by column\nEnter choice:'))
    if n == 1:
        c = input('Enter element symbol:')
        d = 0
        for i in l:
            if i[1] == c:
                print(i)
                d = 1
        if d == 0:
            print('Not found')
    elif n == 2:
        c = input('Enter property:')
        d = 0
        for i in l:
            if i[5] == c:
                print(i)
                d = 1
        if d == 0:
            print('Not found')
    elif n == 3:
        for i in range(len(l)):
            for j in range(len(l) - 1):
                if l[j][2] > l[j + 1][2]:
                    l[j], l[j + 1] = l[j + 1], l[j]
        for i in l:
            print(i)
    elif n == 4:
        c = int(input('Enter row:'))
        d = 0
        for i in l:
            if i[3] == c:
                print(i[0])
                d = 1
        if d == 0:
            print('Not found')
    elif n == 5:
        c = int(input('Enter column:'))
        d = 0
        for i in l:
            if i[4] == c:
                print(i[0])
                d = 1
        if d == 0:
            print('Not found')
    else:
        print('Invalid Choice')

    if input('Do you want to enter more(Y/N)?:')=='Y':
        continue
    else:
        break