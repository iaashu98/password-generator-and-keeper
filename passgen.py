import random
import pickle


dicti={}

with open("pass.me", "br") as readme:
    dicti=pickle.load(readme)
print(dicti)

x= "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?"

lenpass=int(input("Enter desired length\n"))
password= "".join(random.sample(x,lenpass))
print("Your password is: "+password)

prompt=input("\nWould you like to keep this password?\nPress 1 for YES otherwise 2\n")
if("1" in prompt):
    accountinfo=input("Enter the account name for which you want to create a password\n")
    dicti[accountinfo]=password
    with open("pass.me","bw") as myfile:
        pickle.dump(dicti,myfile,protocol=2)

else:
    print("Run Again")
