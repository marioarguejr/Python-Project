#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import random module
import random

#Set input variable to excute dice coding
question = input ('Would you like to roll the dice [y/n]?\n')

#Use while loop to infinitly play dice gamge and determines input is "n" or not. 
#if input is "n", stop while loop and print finish string. 
#if input is not "n", it goes to if condition
while question !='n':
#if input is "y" go to variable 'dice'
    if question == 'y':
#using the random module and randint function to generarte numbers from 1 to 6.
        dice = random.randint (1, 6)
#print random dice between from 1 to 6
        print("You rolled dice at", dice)
#repeat question input variable to excute dice coding again. "y" goes to if condition and play dice again 
#if input is "n" goes to finish and print
        question = input ('Would you like to roll the dice [y/n]?\n')

#Using "else" to detect input errors when a player types a letter that is neither "y" nor "n".
    else:
#display input instruction that "y" and "n"
        print('invalid response. Please type "y" or "n".')
#the question can be repeat it when the player types error
        question = input ('Would you like to roll the dice [y/n]?\n')

#When the player type "n", the output will be that the dice game has finished and then prints 'goodbye string'
print ("Thank you for playing. Goodbye!")


# In[ ]:




