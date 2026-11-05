from getpass import getpass

isLogin = False 

while isLogin == False:
    username = input("input username")
    password = getpass("input password")

    if username == "user1" and password == "Anthonydavis":
        print("access granted")
        isLogin = True
    else:
        print("access denied")
