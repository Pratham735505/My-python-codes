import androidhelper
import time,random
while True:
    droid = androidhelper.Android()
    g=random.randrange(0,10000)%10000
    droid.dialogCreateAlert("Your OTP is "+str(g))
    droid.dialogSetPositiveButtonText('Continue')
  #  droid.makeToast("Your OTP is")
  #  droid.makeToast(str(g))
    droid.dialogShow()
    print("You have 10 seconds to enter otp")
    t1=time.time()
    r=int(input("Enter OTP="))
    t2=time.time()

    if t2-t1>10:
        droid.dialogCreateAlert("Time expired")
        droid.dialogCreateAlert("OTP is sent again")
        droid.dialogSetPositiveButtonText('Continue')
        droid.dialogShow()
        continue 
    
    else:
        if g==r:
            droid.dialogCreateAlert("Verified")
            droid.dialogSetPositiveButtonText('OK')
            droid.dialogShow()
            break
        else:
            droid.dialogCreateAlert("Wrong otp")
            droid.dialogSetPositiveButtonText('OK')
            droid.dialogShow()
            continue
