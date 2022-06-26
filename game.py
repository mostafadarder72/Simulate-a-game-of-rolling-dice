# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 23:19:53 2022

@author: Windows 10
"""

import random 

def Dice_rolls():
    player_rolls = random.randint(1, 6)
    return player_rolls

def main():
    Dice_player_1 = 0
    Dice_player_2 = 0
    Rounds = 0
    Counter_player1_wins = 0
    Counter_player2_wins = 0
    
    print('Hello! What is your name?')
    player_1 = input()
    print('Please enter the name of the competitor?')
    player_2 = input()
    print( player_1 +  ' VS ' + player_2 + '\nATTENTION: Five rounds, the winner is the player who wins three or more rounds.')
    print('The game starts...')
    print()
    for x in range(5):
        Dice_player_1 = Dice_rolls()
        Dice_player_2 = Dice_rolls()
        print( player_1 + " Dice roll number : " + str( Dice_player_1))
        print( player_2 + " Dice roll number : " + str( Dice_player_2))
        
        if Dice_player_1 > Dice_player_2:
                Counter_player1_wins =+ 1
                print(player_1 + " wins in this round!\n")
        elif Dice_player_1 < Dice_player_2:
                Counter_player2_wins =+ 1
                print(player_2 + " wins in this round!\n")
                
        else:
            print("The numbers are the same, try again\n")
            while True:
                Dice_player_1 = Dice_rolls()
                Dice_player_2 = Dice_rolls()
                print( player_1 + " Dice roll number : " + str( Dice_player_1))
                print( player_2 + " Dice roll number : " + str( Dice_player_2))
                if Dice_player_1 > Dice_player_2:
                        Counter_player1_wins =+ 1
                        print(player_1 + " wins in this round!\n")
                        break
                elif Dice_player_1 < Dice_player_2:
                        Counter_player2_wins =+ 1
                        print(player_2 + " wins in this round!\n")
                        break
                if Dice_player_1 == Dice_player_2:
                        continue
            
       
        Rounds =+ 1
       
    if Counter_player1_wins > Counter_player2_wins:
        print(" Dice " + player_1 + " Wins ---> Game winner ")
        print("**Game over**")
    else:
        print("Dice " + player_1 +" Wins ---> Game winner" )
        print("**Game over**")
             
    
main()