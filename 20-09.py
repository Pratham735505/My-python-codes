#Q1
'''
p=set()
o=set()
for i in range(1,101):
    if i%2!=0:
        o.add(i)
    n = i
    g = 0
    while (n > 0):
        if i % n == 0:
            g += 1
        n = n - 1
    if g ==2:
        p.add(i)
print('P U O',p.union(o))
print('P intersection O',p.intersection(o))
print('P-O',p-o)
print('Symmetric difference',(p-o).union(o-p))
'''
#Q2
'''
p=set()
o=set()
for i in range(1,11):
    if i%2==0:
        o.add(i)
for i in range(1,21):
    n = i
    g = 0
    while (n > 0):
        if i % n == 0:
            g += 1
        n = n - 1
    if g!=2:
        p.add(i)
print("All P",all(p))
print("All O",all(o))
print("P superset O",p.issuperset(o))
print("O superset p",o.issuperset(p))
print("Sum of P",sum(p))
print("Sum of O",sum(o))
'''
#Q3
s=set()
c=set()
for i in range(1,11):
    s.add(i**2)
    print(s)
    c.add(i**3)
    print(c)
print("S update",s.update(c))
print("C update",c.update(s))
print(s)
print(c)
print("S remove",s.remove(4))
print("C remove",c.pop())
print(s)
print(c)
print("S discard",s.discard(8))
print("C discard",c.discard(27))
print(s)
print(c)