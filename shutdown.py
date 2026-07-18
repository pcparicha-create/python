def shutdown():
    response = input("are you sure you want to shutdown the system? (yes/no): ")
    if response == "yes":
        print("shutting down...")
    else:
        print("shutdown cancelled.")



def restart():
    response = input("are you sure you want to restart the system? (yes/no): ")
    if response == "yes":
        print("restarting...")
    else:
        print("restart cancelled.")

resp2= input("what do you want to do? (shutdown/restart):")

if resp2 == "shutdown":
    shutdown()
elif resp2 == "restart":
    restart()
else:
    print("invalid option.")



