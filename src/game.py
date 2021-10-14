######################################################################################################################################################
# IMPORTS
######################################################################################################################################################
import random # for choosing dice roll

######################################################################################################################################################
# LIST AND DICTIONARY DECLARATION
######################################################################################################################################################
DICE = [1, 2, 3, 4, 5, 6]

HIGHSCORES = []

######################################################################################################################################################
# MAIN MENU FUNCTIONS
######################################################################################################################################################
def rules():
    print("##### RULES #####\n")
    print("1.) the points rolled on each player's dice are added to their score\n")
    print("2.) if the total number is an even number, an additional 10 points is added to their score\n")
    print("3.) if the total number is an odd number, 5 points are subtracted from their score\n")
    print("4.) if a player rolls a double, they get to roll one extra die and get the number of points added to their score\n")
    print("5.) the score of a player cannot go below 0\n")
    print("6.) the person with the highest score at the end of 5 rounds wins\n")
    print("7.) if both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins)\n")
    print()

    print("returning to main menu...\n")
    mainMenu()


def viewHighScores():
    print("##### LEADERBOARD #####\n")

    highScoreFile = open("assets\highscores.txt", "r") 
    highScores = highScoreFile.readlines()

    for lines in highScores:
        scores = lines.rstrip("\n") # removes \n
        scores = lines.split(",")

        scores[1] = int(scores[1]) # casting the scores into integers
        
        HIGHSCORES.append(scores)
    
    HIGHSCORES.sort(key=lambda index: index[1], reverse=True)

    print(f"first - {HIGHSCORES[0][0]} with a score of {HIGHSCORES[0][1]}\n")
    print(f"second - {HIGHSCORES[1][0]} with a score of {HIGHSCORES[1][1]}\n")     
    print(f"third - {HIGHSCORES[2][0]} with a score of {HIGHSCORES[2][1]}\n")
    print(f"foruth - {HIGHSCORES[3][0]} with a score of {HIGHSCORES[3][1]}\n")
    print(f"fifth - {HIGHSCORES[4][0]} with a score of {HIGHSCORES[4][1]}\n")
    print()
    
    print("returning to main menu...\n")
    mainMenu()


def mainMenu():
    print("########## 2 PLAYER DICE GAME ##########\n")
    
    while True:
        print("1.) continue to login\n")
        print("2.) view high scores\n")
        print("3.) rules\n")
        print("4.) exit program\n")
        userInput = int(input("enter the number of your choice\n"))

        if userInput == 1:
            break
        elif userInput == 2:
            viewHighScores()
            break
        elif userInput == 3:
            rules()
            break
        elif userInput == 4:
            exit()
        else:
            print("error - invalid input\n")
            continue

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
    while True:
        print("##### PLAYER 1 LOGIN #####")
        print("1. create new user\n")
        print("2. use existing user\n")
        userInput = int(input("enter the number of your choice\n"))

        if userInput == 1:
            createUser()
            
            userInput = input("would you like to create another user? yes or no?\n")
            while userInput == "yes":
                createUser()
                userInput = input("would you like to create another user? yes or no?\n")
                if userInput != "yes":
                    break
            
            defaultLogin()
            break
        elif userInput == 2:
            defaultLogin()
            break
        else:
            print("invalid input - try again\n")
            continue


def player2Login():
    while True:
        print("##### PLAYER 2 LOGIN #####")
        print("1. create new user\n")
        print("2. use existing user\n")
        userInput = int(input("enter the number of your choice\n"))

        if userInput == 1:
            createUser()
            
            userInput = input("would you like to create another user? yes or no?\n")
            while userInput == "yes":
                createUser()
                userInput = input("would you like to create another user? yes or no?\n")
                if userInput != "yes":
                    break
            
            defaultLogin()
            break
        elif userInput == 2:
            defaultLogin()
            break
        else:
            print("invalid input - try again\n")
            continue
            
######################################################################################################################################################
# GAME FUNCTIONS
######################################################################################################################################################
def player1Game():
    print("##### PLAYER 1 TURN #####")

######################################################################################################################################################
# MAIN
######################################################################################################################################################
def main():
    # main menu function call
    mainMenu()
    # player login function calls
    player1Login()
    player2Login()
    # game function calls
    player1Game()

######################################################################################################################################################
# RUNNING MAIN FUNCTION
######################################################################################################################################################
if __name__ == "__main__":
    main()

######################################################################################################################################################
# END OF FILE
######################################################################################################################################################