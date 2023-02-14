import androidhelper
droid = androidhelper.Android()
while True:
    g=droid.dialogGetInput("Welcome to my program","1.Registration\n2.Login")
    droid.makeToast("Loading...")
    
    if g.result=='1':
        user=droid.dialogGetInput("Registration Page","Set Username")
        pas=droid.dialogGetInput("Set Password","Password")
        droid.makeToast("Account created")
        droid.makeToast("Going back to Homepage")
 
        continue
    elif g.result=='2':
        respond = droid.dialogGetInput("Login Page", "USER ID")
        if respond.result!=user.result:
            droid.makeToast("Invalid Username or User name does not exist")
            droid.makeToast("Going to homepage")
         
            continue
        p=droid.dialogGetInput("Enter Password","Here:")
  
        if p.result!=pas.result:
            droid.makeToast("Going to homepage")
            continue
        if p.result==pas.result and respond.result==user.result:
            droid.makeToast("Login Successful")
            break
    else:
        droid.makeToast("Invalid Entry")
        break
