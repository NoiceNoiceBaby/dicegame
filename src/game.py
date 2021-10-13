######################################################################################################################################################
# IMPORTS
######################################################################################################################################################
import random # for choosing dice roll

######################################################################################################################################################
# LIST DECLARATION
######################################################################################################################################################
DICE = [1, 2, 3, 4, 5, 6]

######################################################################################################################################################
# LOGIN FUNCTIONS
######################################################################################################################################################
def createUser():
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

        print(f"{username} has been validated\n")

def defaultLogin():
    validationLoop = True
    while validationLoop:
        username = input("enter player username\n")
        password = input("enter player password\n")

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
            userUsername = lines.split(",")
            userPassword = userUsername[1].split("\n")

            if userUsername[0] == username:
                if userPassword[0] == password:
                    print(f"welcome {username}")
                    validationLoop = False
                else:
                    print("incorrect password\n")

        loginFile.close()
        validationLoop = False

    print("exiting player login...\n")

def player1Login():
    print("##### PLAYER 1 LOGIN #####")
    print("1. create new user\n")
    print("2. use existing user\n")
    userInput = int(input())

    if userInput == 1:
        createUser()
        
        userInput = input("would you like to create another user? yes or no?\n")
        while userInput == "yes":
            createUser()
            userInput = input("would you like to create another user? yes or no?\n")
            if userInput != "yes":
                break
        
        defaultLogin()
    elif userInput == 2:
        defaultLogin()

def player2Login():
    print("##### PLAYER 2 LOGIN #####")
    print("1. create new user\n")
    print("2. use existing user\n")
    userInput = int(input())

    if userInput == 1:
        createUser()
        
        userInput = input("would you like to create another user? yes or no?\n")
        while userInput == "yes":
            createUser()
            userInput = input("would you like to create another user? yes or no?\n")
            if userInput != "yes":
                break
        
        defaultLogin()
    elif userInput == 2:
        defaultLogin()
            
######################################################################################################################################################
# GAME FUNCTIONS
######################################################################################################################################################
def player1Game():
    print("##### PLAYER 1 TURN #####")

######################################################################################################################################################
# MAIN
######################################################################################################################################################
def main():
    print("########## DICE GAME ##########")
    # player login function calls
    player1Login()
    player2Login()
    # game
    player1Game()

######################################################################################################################################################
# RUNNING MAIN FUNCTION
######################################################################################################################################################
if __name__ == "__main__":
    main()

######################################################################################################################################################
# END OF FILE
######################################################################################################################################################