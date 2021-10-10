######################################################################################################################################################
# COPYRIGHT 
######################################################################################################################################################

# copyright © 2021 NoiceNoiceBaby

######################################################################################################################################################
# IMPORTS
######################################################################################################################################################
import random # for choosing dice roll

######################################################################################################################################################
# ARRAY DECLARATION
######################################################################################################################################################
DICE = [1, 2, 3, 4, 5, 6]

######################################################################################################################################################
# LOGIN FUNCTIONS
######################################################################################################################################################
def player1Login():
    print("##### PLAYER 1 LOGIN #####")
    print("1. create new user\n")
    print("2. use existing user\n")
    userInput = int(input())

    while userInput == 1:
        createUserLoop = True
        while createUserLoop:
            username = input("enter your username for the new user\n")
            password = input("enter your password for the new user\n")

            confirmUsername = input(f"is {username} your username? yes or no?\n")
            if confirmUsername == "yes":
                confirmPassword = input(f"is {password} your password? yes or no?\n")
                if confirmPassword == "yes":
                    createUserLoop = False
            else:
                continue
            
            loginFile = open("assets\logins.txt", "a")
            loginFile.write(username)
            loginFile.write(",")
            loginFile.write(password)
            loginFile.write("\n") # .write() function only accepts 1 argument... pain
            loginFile.close()

            print("1.) create new user\n")
            print("2.) use existing user\n")
            userInput = int(input())

            if userInput != 1:
                break

        validationLoop = True
        while validationLoop:
            username = input("enter player 1 username\n")
            password = input("enter player 1 password\n")

            confirmUsername = input(f"is {username} your username? yes or no?\n")
            if confirmUsername == "yes":
                confirmPassword = input(f"is {password} your password? yes or no?\n")
                if confirmPassword == "yes":
                    validationLoop = False
            else:
                continue
        
            loginFile = open("assets\logins.txt", "r")
            users = loginFile.readlines()

            for lines in users:
                details = lines.split(",")
                userPassword = details[1].split("\n")

                if details[0] == username:
                    if userPassword[0] == password:
                        print(f"welcome {username}")
                        validationLoop = False
                    else:
                        print("incorrect password\n")
    
            loginFile.close()
            validationLoop = False

        print("exiting player 1 login...\n")
        userInput = False

def player2Login():
    print("##### PLAYER 2 LOGIN #####")
    print("1. create new user\n")
    print("2. use existing user\n")
    userInput = int(input())

    while userInput == 1:
        createUserLoop = True
        while createUserLoop:
            username = input("enter your username for the new user\n")
            password = input("enter your password for the new user\n")

            confirmUsername = input(f"is {username} your username? yes or no?\n")
            if confirmUsername == "yes":
                confirmPassword = input(f"is {password} your password? yes or no?\n")
                if confirmPassword == "yes":
                    createUserLoop = False
            else:
                continue
            
            loginFile = open("assets\logins.txt", "a")
            loginFile.write(username)
            loginFile.write(",")
            loginFile.write(password)
            loginFile.write("\n") # .write() function only accepts 1 argument... pain
            loginFile.close()

            print("1.) create new user\n")
            print("2.) use existing user\n")
            userInput = int(input())

            if userInput != 1:
                break

        validationLoop = True
        while validationLoop:
            username = input("enter player 2 username\n")
            password = input("enter player 2 password\n")

            confirmUsername = input(f"is {username} your username? yes or no?\n")
            if confirmUsername == "yes":
                confirmPassword = input(f"is {password} your password? yes or no?\n")
                if confirmPassword == "yes":
                    validationLoop = False
            else:
                continue
        
            loginFile = open("assets\logins.txt", "r")
            users = loginFile.readlines()

            for lines in users:
                details = lines.split(",")
                userPassword = details[1].split("\n")

                if details[0] == username:
                    if userPassword[0] == password:
                        print(f"welcome {username}")
                        validationLoop = False
                    else:
                        print("incorrect password\n")
    
            loginFile.close()
            validationLoop = False

        print("exiting player 2 login...\n")
        userInput = False
            

######################################################################################################################################################
# MAIN
######################################################################################################################################################
def main():
   print("########## DICE GAME ##########")
   player1Login()
   player2Login()

######################################################################################################################################################
# RUNNING MAIN FUNCTION
######################################################################################################################################################
if __name__ == "__main__":
   main()

######################################################################################################################################################
# END OF FILE
######################################################################################################################################################