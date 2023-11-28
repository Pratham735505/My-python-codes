import random
#filter odd even using lambda
'''
l=[1,2,3,4,5,6,7,8,9,10]
odd=list(filter(lambda x:x%2,l))
even=list(filter(lambda x:True if x%2 ==0 else False,l))
print(odd)
print(even)
'''

#square and cube using lambda
'''
l=[1,2,3,4,5,6,7,8,9,10]
s=list(map(lambda x:x**2,l))
c=list(map(lambda x:x**3,l))
print(f"Cube is {c}")
print(f"Square is {s}")
'''

# Generation of fiboancci using using lambda
'''
n=int(input('Enter fibonacci is to be printed:'))
fib=lambda x,y:x+y
x=0
y=1
print(x)
print(y)
for i in range(n-2):
    z=fib(x,y)
    x=y
    y=z
    print(z)
'''

#Rearranging positive and negative integer in given list using lambda


#program to sort a list of tuple using lambda
#error
'''
l = [('English', 88), ('Science', 99), ('Maths', 97), ('Socialscience', 82)]
s = lambda x, y: x, y = y, x if x[1] > y[1] else ()

for i in range(len(l)):
    for j in range(len(l) - 1):
        s(l[j], l[j + 1])

print(l)
'''
#3 randoms which are divisible by 5 between 100,999
'''
for i in range(3):
    print(random.randrange(100,1000,5))
'''

#accepts a number n and generates a random number having exactly n digits and not starting with zero
'''
n=int(input("Enter number:"))
print(int(random.random()*(10**n)))
'''

#program that inputs two numbers and generates series of random numbers which are divisible by 2 in that range
'''
s=int(input('Enter starting point:'))
e=int(input('Enter ending point:'))
if s%2!=0:
    s+=1
for i in range(10):
    print(random.randrange(s,e,2))
'''

#program to generate 6 digit secured random otp
'''
print('OTP is:',int(random.random()*(10**6)))
'''
'''
s=random.randrange(0,7)
while True:
    print(f'You got {s}')
    e=input('Run again Y/N:')
    if e=='N':
        break
'''