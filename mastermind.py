#----------------------------------------------------------------------------------------------------------#
#CREATOR: beanbeanjuice
#BASED ON: MASTERMIND
#DATE: 11/8/2018
#RESOURCES USED:
#   -1: https://stackoverflow.com/questions/16579085/python-verifying-if-one-list-is-a-subset-of-the-other
#   -2: https://stackoverflow.com/questions/10610158/how-do-i-convert-string-characters-into-a-list
#----------------------------------------------------------------------------------------------------------#

import random
replay = True

while replay == True:

#------------------------------#
    
#-=[VARIABLES]=-#
    red_pegs = (0)
    black_pegs = (0)
    white_pegs = (0)
    opponent_input = ("")
    #colour_list = (["R", "O", "Y", "G", "B", "P", "M", "C"])
    colour_list = ("ROYGBPMC")
    previous_inputs = []
    used_letter_list = ["-"]
    repeat_check = (0)
    playervcomputer = (0)
    opponent_input = ("")
    user_input_list = []

#------------------------------#
    for i in range(0,51):
        print("")
#-=[STARTING SCREEN]=-#
    print("====================================================================================================")
    print("====================================================================================================")
    print("")
    print("""Welcome to Mastermind! The goal of the game is to try to guess the correct colours and colour
before your lives runs out. You have the choice of playing against the computer, or another human!""")
    print("")

#-=[Player or Computer Inputs]=-#
        
    print("====================================================================================================")
    print("====================================================================================================")
    print("")
    playervcomputer = int(input("""Would you like to play against the computer or the player?

1. Computer
2. Player

Choice: """))

    while playervcomputer not in range(1,3):
        for i in range(1, 51):
            print("")
        print("==================================================")
        print("")
        playervcomputer = int(input("""Please select the correct number. Would you like to play against the computer or the player?

1. Computer
2. Player

Choice: """))
        
#------------------------------#
        
#-=[ATTEMPT AMOUNT ("LIVES")]=-#
    for i in range(1, 51):
        print("")
    print("==================================================")
    print("")
    attempts = int(input("""How many attempts would you like...

1. 8 Attempts
2. 10 Attempts
3. 12 Attempts

Choice: """))

    if attempts == (1):
        attempts = (8)
        
    elif attempts == (2):
        attempts = (10)
        
    elif attempts == (3):
        attempts = (12)
            
    while attempts != (8) and attempts != (10) and attempts != (12):
        for i in range(1, 51):
            print("")
        print("")
        print("==================================================")
        attempts = int(input("""Please enter the correct choice of attempts...

1. 8 Attempts
2. 10 Attempts
3. 12 Attempts

Choice: """))
        
        if attempts == (1):
            attempts = (8)
            
        elif attempts == (2):
            attempts = (10)
            
        elif attempts == (3):
            attempts = (12)

#------------------------------#
            
#-=[ASKS THE USER IF REPEATS ARE WANTED]=-#
    for i in range(1, 51):
        print("")
    print("==================================================")
    print("")
    repeats = (str(input("Allow Repeats (Y/N): ")).upper())

    while repeats != "Y" and repeats != "N":
        for i in range(1, 51):
            print("")
        print("==================================================")
        print("")
        repeats = (str(input("""Please enter the correct letter.

Allow Repeats (Y/N): """)).upper())

    if repeats == "N":
        repeats = False
        
    elif repeats == "Y":
        repeats = True

#------------------------------#
        
#-=[ASKS THE USER HOW MANY COLOURS THEY WOULD LIKE (DIFFICULTY)]=-#
    for i in range(1, 51):
        print("")
    print("==================================================")
    print("")
    choice_amount = int(input("""Enter the amount of choices you would like to have...

1. 4 Colour Choices
2. 6 Colour Choices
3. 8 Colour Choices

Choice: """))

    while choice_amount not in range(1, 4):
        for i in range(1, 51):
            print("")
        print("==================================================")
        print("")
        choice_amount = int(input("""Enter the amount of choices you would like to have...

1. 4 Colour Choices
2. 6 Colour Choices
3. 8 Colour Choices

Choice: """))

    if choice_amount == (1):
        choice_amount = 4
        
    elif choice_amount == (2):
        choice_amount = 6
        
    elif choice_amount == (3):
        choice_amount = 8

    if playervcomputer == (1):
        if repeats == False:
            for i in range(1, (choice_amount + 1)):
                x = random.choice(list(colour_list))
                while x in opponent_input:
                    x = random.choice(list(colour_list))
                opponent_input += x
                
        elif repeats == True:
            for i in range(1, (choice_amount + 1)):
                x = random.choice(list(colour_list))
                opponent_input += x

    if playervcomputer == (2):
        if repeats == False:
            while len(opponent_input) != choice_amount or repeat_check != choice_amount or set(list(opponent_input)).issubset(list(colour_list)) == False:
                repeat_check = (0)
                for i in range(1, 51):
                    print("")
                print("==================================================")
                print("OPPONENT INPUTS")
                print("")
                if opponent_input == "HELP":
                    print("EXAMPLE INPUT: ROYG for (Red, Orange, Yellow, Green)")
                opponent_input = str(input("""Please enter a set of %d colours (ROYGBPMC) with no repeats.
Type 'HELP' for more information.

Choice: """ % (choice_amount))).upper()

                for letter in opponent_input:
                    repeat_check += opponent_input.count(letter)
                    
        elif repeats == True:
            while len(opponent_input) != choice_amount or set(list(opponent_input)).issubset(list(colour_list)) == False:
                for i in range(1, 51):
                    print("")
                print("==================================================")
                print("OPPONENT INPUTS")
                print("")
                
                if opponent_input == "HELP":
                    print("EXAMPLE INPUT: ROYG for (Red, Orange, Yellow, Green)")
                opponent_input = str(input("""Please enter a set of %d colours (ROYGBPMC).
Type 'HELP' for more information.

Choice: """ % (choice_amount))).upper()
                
                if opponent_input == "HELP":
                    print("EXAMPLE INPUT: ROYG for (Red, Orange, Yellow, Green)")

#------------------------------#
                    
#-=[DEBUGGING USE]=-#
#REMOVE THE # FROM THE LINE BELOW TO ALLOW
#            print(opponent_input)
                    
#------------------------------#
                    
#-=[MAKING SURE CONDITIONS ARE MET BEFORE CONTINUING]=-#
    while red_pegs != choice_amount and attempts != 0:

#------------------------------#
        
#-=[ASKING USER FOR COLOUR INPUT]=-#
        for i in range(1, 100):
            print("")
        print("==================================================")
        print("")
        print("You have %d attempts left" % (attempts))
        print("")
        print("-=[|||||||||||||||||PREVIOUS INPUTS|||||||||||||||||]=-")
        for num, i in enumerate(reversed(previous_inputs)):
            print("%i -> %s" % ((num - len(previous_inputs)) * -1, i))
        print("-=[|||||||||||||||||||||||||||||||||||||||||||||||||]=-")
        print("")
        user_input = (str(input("""Please enter a set of colours. Type 'HELP' for more information.

Colours (%s): """ % (colour_list))).upper())

#------------------------------#
        
#-=[MAKING SURE USER'S INPUT FOLLOWS THE RULES BASED ON PREVIOUS CHOICES]=-#
        if repeats == False:
            repeat_check = (0)
            for letter in user_input:
                repeat_check += user_input.count(letter)
            if repeat_check != choice_amount:
                    print("Please enter a set of colours with NO repeats.")

        while set(list(user_input)).issubset(list(colour_list)) == False or len(user_input) != choice_amount or (repeats == False and repeat_check != choice_amount):
            repeat_check = (0)
            user_input = (str(input("""Please enter a set of colours. Type 'HELP' for more information.

Colours (%s): """ % (colour_list))).upper())
            if user_input == ("HELP"):
                print("Format Example: 'ROYG' for 'Red, Orange, Yellow, Green'")

            elif len(user_input) != choice_amount:
                print(("Please enter the correct amount of %d colours.") % (choice_amount))

            elif set(list(user_input)).issubset(list(colour_list)) == False:
                print("Please enter a set of colours in (ROYGBPMC)")
                
            if repeats == False and repeat_check != choice_amount:
                print("Please enter a set of colours with NO repeats.")
            
            for letter in user_input:
                repeat_check += user_input.count(letter)
                
#------------------------------#

#-=[RESETTING DATA]=-#
        red_pegs = 0
        white_pegs = 0
        black_pegs = 0
        opponent_input_list = list(opponent_input)
        user_input_list = list(user_input)

#------------------------------#

#-=[CHECKING IF USER DATA CORRESPONDS WITH COMPUTER/OPPONENT DATA]=-#
        for num, letter in enumerate(opponent_input_list):
            if user_input_list[num] == letter:
                red_pegs += 1
                user_input_list[num] = ("-")
#                opponent_input_list[num] = ("-")
        
        for num, letter in enumerate(opponent_input_list):
            if (user_input_list.count(letter) > opponent_input_list.count(letter)) and user_input_list[num] in opponent_input_list and user_input_list[num] != ("-"):
#                print("FIRST")
                white_pegs += opponent_input_list.count(letter)
                for u_num, u_letter in enumerate(user_input_list):
                    if u_letter == letter:
                        user_input_list[u_num] = ("-")
                for c_num, c_letter in enumerate(opponent_input_list):
                    if c_letter == letter:
                        opponent_input_list[c_num] = ("-")

            elif user_input_list.count(letter) <= opponent_input_list.count(letter) and letter not in used_letter_list and user_input_list[num] in opponent_input_list:
#                print("SECOND")
                white_pegs += 1
                user_input_list[num] = ("-")

        black_pegs = ((choice_amount) - (red_pegs + white_pegs))
#        white_pegs -= black_pegs
#        black_pegs = ((choice_amount) - (red_pegs + white_pegs))

#------------------------------#

#-=[APPENDS USER'S PREVIOUS INPUTS TO A LIST]=-#
        previous_inputs.append(("%s - Red Pegs: %d, White Pegs: %d, Black Pegs: %d" % (user_input, red_pegs, white_pegs, black_pegs)))
        attempts -= (1)

#------------------------------#
        
#-=[GAME ENDING SEQUENCES]=-#
    if attempts == 0:
        for i in range(1, 51):
            print("")
        print("==================================================")
        print("")
        print("-=[|||||||||||||||||PREVIOUS INPUTS|||||||||||||||||]=-")
        for num, i in enumerate(reversed(previous_inputs)):
            print("%i -> %s" % ((num - len(previous_inputs)) * -1, i))
        print("-=[|||||||||||||||||||||||||||||||||||||||||||||||||]=-")
        print("")
        print("Sorry... you're bad at this.")
        print("The correct answer is %s." % (opponent_input))
        print("")
        print("==================================================")
        
    if red_pegs == choice_amount:
        for i in range(1, 51):
            print("")
        print("==================================================")
        print("")
        print("-=[|||||||||||||||||PREVIOUS INPUTS|||||||||||||||||]=-")
        for num, i in enumerate(reversed(previous_inputs)):
            print("%i -> %s" % ((num - len(previous_inputs)) * -1, i))
        print("-=[|||||||||||||||||||||||||||||||||||||||||||||||||]=-")
        print("")
        print("You win! Total Attempts Remaining: %d" % (attempts))
        print("")
        print("==================================================")
        print("")

#------------------------------#

#-=[REPLAY]=-#
    replay = str(input("Would you like to play again? (Y/N): ")).upper()

    if replay == ("Y"):
        replay = True
        
    if replay == ("N"):
        replay = False
