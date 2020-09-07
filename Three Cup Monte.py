# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 20:31:17 2020

@author: Admin
"""

#Three Cup Monte

from random import shuffle

#To shuffle the list randomly
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

#Input Player Guess
def player_guess():
    guess= None
    while guess not in [0,1,2]:
        guess=int(input('Enter your index guess? '))
    return guess

#Check the guess
def check_guess(mylist, guess):
    if mylist[guess]=='O':
        print('YOU HAVE GUESSED IT RIGHT')
        print(mylist)
    else:
        print('WRONG GUESS')
        print(mylist)
        
#Time to Play
mylist=['','O','']
final_list = shuffle_list(mylist)
user_guess = player_guess()
check_guess(final_list, user_guess)


  

