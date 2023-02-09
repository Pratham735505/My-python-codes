import time,random
while True:
    g=random.randrange(0,10000)%10000
    print("Your otp is=",g)
    print("You have 10 seconds to enter otp")
    t1=time.time()
    r=int(input("Enter OTP="))
    t2=time.time()

    if t2-t1>10:
        print("Time expired")
        print("OTP is sent again")
        continue 
    
    else:
        if g==r:
            print("Verified")
            break
        else:
            print ("Wrong otp")
            continue
