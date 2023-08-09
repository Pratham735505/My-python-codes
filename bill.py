unit=eval(input("Enter number of units:"))
if unit<200:
    total=1.2*unit
elif unit>=200 and unit<400:
    total=1.5*unit
elif unit>=400 and unit<600:
    total=1.8*unit
else:
    total=2*unit


if total>400:
    total=total+total*0.15

if total<=100:
    total=100

print("Total bill is:",total)
