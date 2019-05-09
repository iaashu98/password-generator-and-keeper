import getpass
import pickle

masterpass= input("Enter Your Master Password\n")

if masterpass=="12345":
    acc_name=input("Enter Your Account Name")
    with open("pass.me", "br") as readme:
       dicti=pickle.load(readme)

    if acc_name in dicti:
        password=getpass.dicti[acc_name]
    print("Password= ",password)

