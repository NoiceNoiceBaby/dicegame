######################################################################################################################################################
# IMPORTS
######################################################################################################################################################
import random # for choosing dice roll
import time # for sleep
from os import system, name # for clearing terminal screen

######################################################################################################################################################
# SYSTEM
######################################################################################################################################################
def clearScreen():
    # if the system which the code is being ran on is a windows one
    if name == "nt":
        _ = system('cls')
    # if the system which the code is being ran on is a linux/mac one
    else:
        _ = system('clear')

# credits: https://www.geeksforgeeks.org/clear-screen-python/

######################################################################################################################################################
# LIST DECLARATION
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

    time.sleep(3)
    
    print("returning to main menu...\n")
    clearScreen()
    mainMenu()


def viewHighScores():
    print("##### LEADERBOARD #####\n")

    highScoreFile = open("assets\highscores.txt", "r") 
    highScores = highScoreFile.readlines()

    for lines in highScores:
        scores = lines.rstrip("\n") # removes \n
        scores = lines.split(",")

        scores[1] = int(scores[1]) # casting the scores into integers so they can be sorted accordingly
        
        HIGHSCORES.append(scores)
    
    HIGHSCORES.sort(key=lambda index: index[1], reverse=True)

    print(f"first - {HIGHSCORES[0][0]} with a score of {HIGHSCORES[0][1]}\n")
    print(f"second - {HIGHSCORES[1][0]} with a score of {HIGHSCORES[1][1]}\n")     
    print(f"third - {HIGHSCORES[2][0]} with a score of {HIGHSCORES[2][1]}\n")
    print(f"foruth - {HIGHSCORES[3][0]} with a score of {HIGHSCORES[3][1]}\n")
    print(f"fifth - {HIGHSCORES[4][0]} with a score of {HIGHSCORES[4][1]}\n")
    print()
    
    time.sleep(3)

    print("returning to main menu...\n")
    clearScreen()
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
            clearScreen()
            break
        elif userInput == 2:
            clearScreen()
            viewHighScores()
            break
        elif userInput == 3:
            clearScreen()
            rules()
            break
        elif userInput == 4:
            clearScreen()
            exit()
        else:
            print("error - invalid input\n")
            clearScreen()
            continue

######################################################################################################################################################
# LOGIN FUNCTIONS
######################################################################################################################################################
def createUser():
    createUserLoop = True
    while createUserLoop:
        clearScreen()
        username = input("enter your username for the new user\n")
        password = input("enter your password for the new user\n")

        confirmUsername = input(f"is {username} your username? yes or no?\n")
        if confirmUsername == "yes":
            confirmPassword = input(f"is {password} your password? yes or no?\n")
            if confirmPassword == "yes":
                createUserLoop = False
            else:
                clearScreen()
                continue
        else:
            clearScreen()
            continue
        
        loginFile = open("assets\logins.txt", "a")
        loginFile.write(username)
        loginFile.write(",")
        loginFile.write(password)
        loginFile.write("\n") # .write() function only accepts 1 argument... pain
        loginFile.close()

        print(f"{username} has been validated\n")
        time.sleep(0.5)

def defaultLogin():
    validationLoop = True
    while validationLoop:
        clearScreen()
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
                    time.sleep(0.5)
                    validationLoop = False
                else:
                    print("incorrect password\n")
                    clearScreen()
                    continue
            else:
                print("incorrect username\n")
                clearScreen()
                continue

        loginFile.close()
        validationLoop = False

    print("exiting player login...\n")

def player1Login():
    while True:
        clearScreen()
        print("##### PLAYER 1 LOGIN #####")
        print("1. create new user\n")
        print("2. use existing user\n")
        userInput = int(input("enter the number of your choice\n"))

        if userInput == 1:
            createUser()
            
            userInput = input("would you like to create another user? yes or no?\n")
            while userInput == "yes":
                clearScreen()
                createUser()
                userInput = input("would you like to create another user? yes or no?\n")
                if userInput != "yes":
                    clearScreen()
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
        clearScreen()
        print("##### PLAYER 2 LOGIN #####")
        print("1. create new user\n")
        print("2. use existing user\n")
        userInput = int(input("enter the number of your choice\n"))

        if userInput == 1:
            createUser()
            
            userInput = input("would you like to create another user? yes or no?\n")
            while userInput == "yes":
                clearScreen()
                createUser()
                userInput = input("would you like to create another user? yes or no?\n")
                if userInput != "yes":
                    clearScreen()
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
def scoreSystem(score):
    if score % 2 == 0:
        score = score + 10
    else:
        score = score - 5 
        if score < 0:
            score = score + 5
    
    return score

def rounds():
    clearScreen()
    print("ready to roll the dice!\n")
    
    diceRoll = random.choice(DICE)

    while diceRoll == 6:
        diceRoll = random.choice(DICE)
        if diceRoll !=6:
            break
    
    scoreSystem(diceRoll)

def player1Game():
    clearScreen()
    print("##### PLAYER 1 TURN #####")
    
    roundCount = 0
    while roundCount > 6:
        rounds()
        roundCount = roundCount + 1
    
    clearScreen()
    #print(f"player 1 finished wiht a score of {score}\n")

def player2Game():
    clearScreen()
    print("##### PLAYER 2 TURN #####")
    
    roundCount = 0
    while roundCount > 6:
        rounds()
        roundCount = roundCount + 1
    
    clearScreen()
    #print(f"player 2 finished with a score of {score}\n")

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