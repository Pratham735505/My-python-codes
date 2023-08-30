import time
import os,subprocess
def countdown(t):
    while t:
        print("\n" * 5)
        mins,secs=divmod(t,60)
        timer ='{:02d}:{:02d}'.format(mins,secs)
        print(timer)
        time.sleep(1)
        t-=1
    print("\n" * 5)

    print('Fire in the hole')
t=input("Enter the time in seconds:")
print("\n" * 5)
countdown(int(t))
