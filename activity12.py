import getpass

username = "pogiako2026"
password = "pogiako2026"

u = input("Enter username ----> ")
p = getpass.getpass("Enter password ----> ")

if username == u and password == p:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")