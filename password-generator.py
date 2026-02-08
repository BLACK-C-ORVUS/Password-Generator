from random import sample
from string import ascii_letters
from datetime import datetime
import os
# character sets
char = ascii_letters
symbol = "~@#$%^&*()}/}"
number = "0123456789"

ALL_CHARS = char + symbol + number
password = None

# Generat password
def generat_paa(ALL_CHARS):
    """
    Generate a random password based on user-defined length.

    Args:
        ALL_CHARS (String): character sets

    Returns:
       String : Generated password

    """
    length = int(input("Enter the lenght of password : "))
    if length >= 1 :
        global password
        password = "".join(sample(ALL_CHARS, length))
        print(f"\n Your password is :{password}\n")
        return password

    else:
        print("\nPassword lengtht must be greater then 0!\n")
# Save password to file
def save_pass(password):
    """
    Save the generated password with username and comment to text file.
    Args:
        password (String): Generated password

    """
    now = datetime.today()
    time = now.strftime("%Y/%b/%d - %H:%M")
    user = input("Enter username for this password : ")
    comment = input("Enter a commnet for this password : ")
    save = open("password.txt", "a")
    save.write(f"\n{comment} : {user} == {password} , DateTime ==  {time}")
    save.close() 



# Min menu loop
while True :
    os.system("clear")
    print("Choose on option : \n\t1) Create a password\n\t2) Exit\n")
    choice = input("Your choice : ") 

    if choice == "1":
        generat_paa(ALL_CHARS)
        choice_save = input("Do you want save password? [Y/n]: ")

        if choice_save.lower() == "y":
            save_pass(password)

        elif choice_save.lower() == "n":
            print("Goodbye...")
            break
        else:
            print("Invalid choice!\n")


    elif choice == "2":
        print("Goodbye...")
        break
    else:
        print("\n Invalid choice! \n")
    

