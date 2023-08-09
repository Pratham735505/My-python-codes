'''program to find the net salary of an employee'''

name = input("Enter the Name:")
grade = input("Enter the grade:")
invalid =  0
fa = 0

if(grade == 'a' or grade == 'A'):
    sal = int(input("Enter the salary (35k - 40k):"))
    if(sal > 35000 and sal <= 40000):
        ta = (70/100)*sal
        da = (80/100)*sal
        pf = (30/100)*sal
    else:
        print("wrong salary")
        invalid = 1
        
elif(grade == 'b' or grade == 'B'):
    sal = int(input("Enter the salary (25k - 35k):"))
    if(sal > 25000 and sal <= 35000):
        ta = (50/100)*sal
        da = (60/100)*sal
        pf = (20/100)*sal
    else:
        invalid = 1

elif(grade == 'c' or grade == 'C'):
    sal = int(input("Enter the salary (15k - 25k):"))
    if(sal > 15000 and sal <= 25000):
        ta = (35/100)*sal
        da = (45/100)*sal
        pf = (10/100)*sal
    else:
        invalid = 1

elif(grade == 'd' or grade == 'D'):
    sal = int(input("Enter the salary (15k - 25k):"))
    if(sal > 12000 and sal <= 15000):
        fa = (20/100)*sal
        ta = 0
        da = 0
        pf = 0
    else:
        invalid = 1

else:
    print("Invalid Grade")

if(invalid == 0):
    print("Net salary:", sal+ta+da+fa-pf)
else:
    print("Invalid salary")
    
    
