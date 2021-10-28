######################################################################################################################################################
# IMPORTS
######################################################################################################################################################
import random # for choosing dice roll
import time # for sleep
import os # for clearing terminal screen and file checks

######################################################################################################################################################
# SYSTEM 
######################################################################################################################################################
def clearScreen():
    # if the system which the code is being ran on is a windows one
    if os.name == "nt":
        _ = os.system('cls')
    # if the system which the code is being ran on is a linux/mac one
    else:
        _ = system('clear')

######################################################################################################################################################
# LIST DECLARATION
######################################################################################################################################################
DICE = [1, 2, 3, 4, 5, 6]

USERNAMES = []
PASSWORDS = []

USERNAMES_IN_USE = []

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

    time.sleep(3)
    
    print("returning to main menu...\n")
    clearScreen()
    mainMenu()


def viewHighScores():
    print("##### LEADERBOARD #####\n")

    highScoresFile = open("assets\highscores.txt")
    highScores = highScoresFile.readlines()

    for lines in highScores:
        scores = lines.rstrip("\n") 
        scores = lines.split(",")

        scores[1] = int(scores[1]) 
        
        HIGHSCORES.append(scores)
    
    HIGHSCORES.sort(key=lambda index: index[1], reverse=True)

    print(f"first - {HIGHSCORES[0][0]} with a score of {HIGHSCORES[0][1]}\n")
    print(f"second - {HIGHSCORES[1][0]} with a score of {HIGHSCORES[1][1]}\n")     
    print(f"third - {HIGHSCORES[2][0]} with a score of {HIGHSCORES[2][1]}\n")
    print(f"foruth - {HIGHSCORES[3][0]} with a score of {HIGHSCORES[3][1]}\n")
    print(f"fifth - {HIGHSCORES[4][0]} with a score of {HIGHSCORES[4][1]}\n")
    
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

        try:
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
                print("thank you for playing the dice game\n")
                time.sleep(1)
                exit()
        
        except ValueError:
            print("invalid input\n")
            time.sleep(0.5)
            continue

######################################################################################################################################################
# LOGIN FUNCTIONS
######################################################################################################################################################
def createUser():
    while True:
        clearScreen()
        username = input("enter your username for the new user\n")
        password = input("enter your password for the new user\n")

        confirmUsername = input(f"is {username} your username? yes or no?\n")
        if confirmUsername == "yes":
            confirmPassword = input(f"is {password} your password? yes or no?\n")
            if confirmPassword == "yes":
                pass
            else:
                clearScreen()
                continue
        else:
            clearScreen()
            continue
        
        loginFile = open("assets\logins.txt", "r")
        users = loginFile.readlines()

        for lines in users:
            userInfo = lines.strip("\n").split(",")

            user_name = userInfo[0]
            
            USERNAMES.append(user_name)
        
        loginFile.close()

        if username in USERNAMES:
            print("username is already taken")
            time.sleep(0.5)
            continue
        else:
            loginFile = open("assets\logins.txt", "a")
            loginFile.write(username)
            loginFile.write(",")
            loginFile.write(password)
            loginFile.write("\n")
            loginFile.close()
            
            print(f"{username} has been validated\n")
            time.sleep(0.5)
            break
            
def checkUser(username, password):
    loginFile = open("assets\logins.txt", "a+")
    users = loginFile.readlines()

    for i in HIGHSCORES:
        del(HIGHSCORES[i])
    
    if username in USERNAMES_IN_USE:
        print("user already in use\n")
        time.sleep(0.5)
        loginMenu()
        clearScreen()
    else:
        for lines in users:
            userInfo = lines.strip("\n").split(",")

            user_name = userInfo[0]
            user_password = userInfo[1]

            USERNAMES.append(user_name)
            PASSWORDS.append(user_password)

        if username in USERNAMES:
            usernamePos = USERNAMES.index(username)
            
            try:
                passwordPos = PASSWORDS.index(password)

                if usernamePos == passwordPos:
                    print(f"welcome {username}")
                    USERNAMES_IN_USE.append(username)
                    time.sleep(0.5)
                    clearScreen()
            
            except ValueError:
                print("incorrect password\n")
                time.sleep(0.5)
                clearScreen()
                loginMenu()

        else:
            print("incorrect username\n")
            time.sleep(0.5)
            clearScreen()
            loginMenu()
    
    loginFile.close()

def player1Login():
    while True:
        print("##### PLAYER 1 LOGIN #####")
    
        global player1Username, player1Password
        
        player1Username = input("enter player username\n")
        player1Password = input("enter player password\n")

        confirmUsername = input(f"is {player1Username} your username? yes or no?\n")
        if confirmUsername == "yes":
            confirmPassword = input(f"is {player1Password} your password? yes or no?\n")
            if confirmPassword == "yes":
                checkUser(player1Username, player1Password)
                break

            else:
                continue
        else:
            continue

def player2Login():
    while True:
        print("##### PLAYER 2 LOGIN #####")

        global player2Username, player2Password
        
        player2Username = input("enter player username\n")
        player2Password = input("enter player password\n")

        confirmUsername = input(f"is {player2Username} your username? yes or no?\n")
        if confirmUsername == "yes":
            confirmPassword = input(f"is {player2Password} your password? yes or no?\n")
            if confirmPassword == "yes":
                checkUser(player2Username, player2Password)
                break

            else:
                continue
        else:
            continue

def loginMenu():
    print("##### LOGIN MENU #####\n")
    print("1.) create user\n")
    print("2.) player 1 login\n")
    print("3.) player 2 login\n")

    userInput = int(input("enter a number of your choice\n"))

    if userInput == 1:
        clearScreen()
        createUser()
        userInput = input("would you like to create another user? yes or no?\n")

        while userInput == "yes":
            clearScreen()
            createUser()
            userInput = input("would you like to create another user? yes or no?\n")

            if userInput != "yes":
                clearScreen()
                break
        
        loginMenu()
    
    elif userInput == 2:
        player1Login()
    
    elif userInput == 3:
        player2Login()

######################################################################################################################################################
# GAME FUNCTIONS
######################################################################################################################################################
def scoreSystem(score):
    diceRoll = random.choice(DICE)
    
    while diceRoll == 6:
        diceRoll = random.choice(DICE)
        if diceRoll != 6:
            break

    score = score + diceRoll
    
    if score % 2 == 0:
        score = score + 10
    else:
        score = score - 5
        if score < 0:
            score = score + 5
    
    return score

def submitScore(score):
    clearScreen()
    
    score = str(score) # cast score to a string so it can be appended to the file
    username = input("which display name do you want in the highscores file?\n")

    highScoreFile = open("assets\highscores.txt", "a") 
    highScoreFile.write(username)
    highScoreFile.write(",")
    highScoreFile.write(score)
    highScoreFile.write("\n") # .write() function only accepts 1 argument... pain
    highScoreFile.close()

    userInput = input("would you like to see the top 5 scores? yes or no?\n")

    if userInput == "yes":
        viewHighScores()
    else:
        print("thank you for playing the dice game!\n")

def player1Game():
    clearScreen()
    print("##### PLAYER 1'S TURN #####\n")

    player1Score = 0
    roundCount = 1
    
    while roundCount < 6:
        player1Score = scoreSystem(player1Score)
        print(f"round {roundCount} complete! you finished this round with a score of {player1Score}!\n")
        
        time.sleep(1)
        
        global player1FinalScore
        player1FinalScore = player1Score
        
        roundCount = roundCount + 1

    time.sleep(3)
    clearScreen()
    
def player2Game():
    clearScreen()
    print("##### PLAYER 2'S TURN #####\n")

    player2Score = 0
    roundCount = 1
    
    while roundCount < 6:
        player2Score = scoreSystem(player2Score)
        print(f"round {roundCount} complete! you finished this round with a score of {player2Score}!\n")
        
        time.sleep(1)
        
        global player2FinalScore
        player2FinalScore = player2Score
        
        roundCount = roundCount + 1

    time.sleep(3)
    clearScreen()

def postGame():
    clearScreen()
    print("##### POST GAME SCREEN #####")
    
    if player1FinalScore > player2FinalScore:
        print("congratulations! player 1 won!\n")
        
        time.sleep(1.5)
        
        clearScreen()
        submitScore(player1FinalScore)
    
    elif player2FinalScore > player1FinalScore:
        print("congratulations! player 2 won!\n")

        time.sleep(1.5)
        
        clearScreen()
        submitScore(player2FinalScore)
    
    else:
        player1Decider = scoreSystem(player1FinalScore)
        player2Decider = scoreSystem(player2FinalScore)

        if player1Decider > player2Decider:
            print("after a close game, player 1 is the winner!\n")

            time.sleep(1.5)
        
            clearScreen()
            submitScore(player1Decider)

        elif player2Decider > player1Decider:
            print("after a close game, player 2 is the winner!\n")

            time.sleep(1.5)
        
            clearScreen()
            submitScore(player2Decider)
        else:
            print("unfortunate! both players tied!\n")
            
            time.sleep(1.5)
            clearScreen()
            
            print("thank you for playing the dice game!\n")
    
######################################################################################################################################################
# MAIN
######################################################################################################################################################
def main():
    # main menu function call
    mainMenu()
    # player login function calls
    loginMenu()
    # game function calls
    #player1Game()
    #player2Game()
    #postGame()

######################################################################################################################################################
# RUNNING MAIN FUNCTION
######################################################################################################################################################
if __name__ == "__main__":
    main()

######################################################################################################################################################
# END OF FILE
######################################################################################################################################################