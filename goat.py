#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
***************************************************************************
Filename:      goat.py

Author:        John Vicino

Date:          2020.08.06

Modifications:  none

Description:   This program runs the Monty Hall gameshow.
               The user inputs a number of games to play. 
               For each game a door is chosen 1-3. 
               The host then reveals a goat behind another door.
               The contestant can choose to switch to the other remaining door.
               If the car is won, the game is marked as a win.
               If a goat is won, the game is not marked as a win. 
               It calculates the win percentage of the number of games. 
               To automatically play, uncomment the auto selection and auto switch,
               and comment out the manual selection and switch. 
              
***************************************************************************
"""
import random

wins = 0.0  # Number of wins 

total_games = float(input("How many games would you like to play?: ")) # Number of total games to play

prizes = ['car', 'goat', 'goat']  # Prizes for the game                     

count = 1 # Game number


# loops the game the number for the number of total games selected
for games in range (int(total_games)):
    
    # Start a new game and print out the number
    print("\nNEW GAME: ", count)

    # Door with the goat behind it
    goat_door = 0              
    
    
    # shuffles the prizes to new doors
    random.shuffle(prizes)
    
    
    # Door assigned to prizes
    doors = {                           
      '1': prizes[0], 
      '2': prizes[1], 
      '3': prizes[2]
    }
    
    # Stores the remaining doors and prizes after the switch
    doors_after_switch = {}     
    
    # Manual selection of door. 
    selection = eval(input("Please enter a door (1, 2, or 3): "))
    
    # auto selection of a door
#    selection = random.randint(1,3)
  
    
    print("Door selected: ", selection)
    
    # finds the door for the host to reveal
    for num, prize in doors.items():
        
        # Sets the door the host will open 
        if ((int(num) != int(selection) and prize == 'goat') and goat_door == 0):
            goat_door = num

        # dictionary of the remaining doors
        else: 
            doors_after_switch[num] = prize

    # Host opens a door with a goat and contestant changes selection
    print("\nHost shows the goat behind door: {}.".format(goat_door))

    # Auto switch door
#    switch  = random.choice(['y', 'n'])
    
    # Manual switch door
    switch = (input("Would you like to switch your door? (y/n): ").lower())
    
    if (switch == 'n'):
        prize_won = doors_after_switch[str(selection)]
        
    
    else: 
        print ("\nContestant switches their door!")
        
        # switches the door and assigns the prize
        for key, item in doors_after_switch.items():
            
            if (int(key) != int(selection)):
                print ("New door is: {}\n".format(key))
                prize_won = item
            
            else:
                continue
    
    # Counts wins and losses
    if (prize_won == 'car'):
        print("You won the CAR! Congratulations!")
        wins += 1.0
    else:
        print ("You got the GOAT! Bahhhter luck next time!")
    
    # Next game number
    count += 1

        

# Outputs the total number of games won, played and the win percentage  
print ("\nContestant played {} and won {} games".format(int(total_games), int(wins)))    
print ("The win percentage was {}%".format(round((wins/total_games)*100.0, 2)))



"""
Output:

How many games would you like to play?: 4

NEW GAME:  1

Please enter a door (1, 2, or 3): 1
Door selected:  1

Host shows the goat behind door: 2.

Would you like to switch your door? (y/n): y

Contestant switches their door!
New door is: 3

You won the CAR! Congratulations!

NEW GAME:  2

Please enter a door (1, 2, or 3): 2
Door selected:  2

Host shows the goat behind door: 1.

Would you like to switch your door? (y/n): y

Contestant switches their door!
New door is: 3

You won the CAR! Congratulations!

NEW GAME:  3

Please enter a door (1, 2, or 3): 3
Door selected:  3

Host shows the goat behind door: 1.

Would you like to switch your door? (y/n): n
You got the GOAT! Bahhhter luck next time!

NEW GAME:  4

Please enter a door (1, 2, or 3): 1
Door selected:  1

Host shows the goat behind door: 2.

Would you like to switch your door? (y/n): n
You got the GOAT! Bahhhter luck next time!

Contestant played 4 and won 2 games
The win percentage was 50.0%
"""