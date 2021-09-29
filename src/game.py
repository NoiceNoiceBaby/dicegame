######################################################################################################################################################
# IMPORTS
######################################################################################################################################################
import json # database
import random # for choosing dice roll

######################################################################################################################################################
# ARRAY DECLARATION
######################################################################################################################################################
DICE = [1, 2, 3, 4, 5, 6]

######################################################################################################################################################
# LOGIN
######################################################################################################################################################
def login():
    print("1. create new user\n")
    print("2. use existing user\n")
    userInput = int(input())

    if userInput == 1:
        validationLoop = True
        while validationLoop:
            username = input("enter your username\n")
            password = input("enter your password\n")

            confirmUsername = input(f"is {username} your username? yes or no?\n")
            if confirmUsername == "yes":
                confirmPassword = input(f"is {password} your password? yes or no?\n")
                if confirmPassword == "yes":
                    validationLoop = False
            else:
                continue

        with open("src/assets/logins.json", "r") as loginsFile:
            logins = json.load(loginsFile)

            logins[str(username)] = str(password)

            with open("src/assets/logins.json", "a") as loginsFile:
                json.dump(logins, loginsFile)
                del [logins]

    elif userInput == 2:
        validationLoop = True
        while validationLoop:
            username = input("enter your username\n")
            password = input("enter your password\n")

            confirmUsername = input(f"is {username} your username? yes or no?\n")
            if confirmUsername == "yes":
                confirmPassword = input(f"is {password} your password? yes or no?\n")
                if confirmPassword == "yes":
                    validationLoop = False
            else:
                continue
        
        with open("src/assets/logins.json", "r") as loginsFile:
            logins = json.load(loginsFile)
 
            if username in logins:
                if password in logins:
                    print(f"access granted - welcome {username}\n")
                else:
                    print("error - incorrect password\n")
            else:
                print("error - incorrect username\n")
    else:
        print("error - invalid input\n")
            

######################################################################################################################################################
# MAIN
######################################################################################################################################################
def main():
   print("########## DICE GAME ##########")
   login()

######################################################################################################################################################
# RUNNING MAIN FUNCTION
######################################################################################################################################################
if __name__ == "__main__":
   main()

######################################################################################################################################################
# END OF FILE
######################################################################################################################################################