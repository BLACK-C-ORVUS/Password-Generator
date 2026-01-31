from random import sample
from string import ascii_letters
from datetime import datetime
# create datda 
char = ascii_letters
symbol = "~@#$%^&*()}/}"
number = "0123456789"
all = char + symbol + number

# genrat password
def generat_paa(all):
    length = int(input("Enter the lenght of Password : "))
    if length >= 1 :
        password = "".join(sample(all, length))
        print(f"\n Your password is :{password}\n")
        return password

    else:
        print("\nYour number olded 0 \n")
# save password
def save_pass(password):
    now = datetime.today()
    time = now.strftime("%Y/%b/%d - %H:%M")
    user = input("Enter username for password : ")
    comment = input("Enter commnet for password : \n")
    save = open("password.txt", "a")
    save.write(f"\n{comment} : {user} == {password} , DateTime ==  {time}")
    save.close() 




while True :
    print("Choose on Option : \n\t1)Create a Password\n\t2)Exit")
    choice = input("Your Choice : ")

    if choice == "1":
        generat_paa(all)
        choice_save = input("Do you whant save password? [Y/n]")

        if choice_save.lower() == "y":
            save_pass()

        elif choice_save.lower() == "n":
            break
        else:
            print("Your choice is Wrong!\n")


    elif choice == "2":
        print("Good By...")
        break
    else:
        print("\n Your choice is Wrong! \n")
    

