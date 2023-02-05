def isempty():
  if len(a)==0:
    return True
  else:
    return False
def push():
  if len(a)==5:
    print("Overflow")
  else:
    item=int(input("Enter value to be pushed:"))
    a.append(item)
def pop():
  if isempty():
    print("Underflow")
  else:
    g=a.pop()
    print("Popped element is ",g)
def display():
  if isempty():
    print("Underflow")
  else:
    i=len(a)-1
    while i>=0:
      if i==len(a)-1:
        print(a[i],"<--top")
      else:
        print(a[i])
      i=i-1
a=[]
while True:
  print("1.Push\n2.Pop\n3.Display")
  choice=int(input("Enter choice:"))
  if(choice==1):
    push()
  elif choice==2:
    pop()
  elif choice==3:
    display()
  else:
    print("Invalid choice")
  ch=input("Do you want to run again y/n?=")
  if ch=='y' or ch=='Y':
    continue
  else:
    break
  

