#******************************************************************************
# binary.py
#******************************************************************************
# Name: Jake Yashayev
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
# NONE
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
# 
# 
import random

#random generation of 8 bits
eighth = random.randrange(0,2)
seventh = random.randrange(0,2)
sixth = random.randrange(0,2)
fifth = random.randrange(0,2)
fourth = random.randrange(0,2)
third = random.randrange(0,2)
second = random.randrange(0,2)
first = random.randrange(0,2)

binnum = f'{eighth}{seventh}{sixth}{fifth}.{fourth}{third}{second}{first}'
print(f'Here\'s a random example of binary!\nThe binary number {binnum} is the same as the decimal number ', end = '')


#kinda messy, would prefor for loop on array, but works
decimal = eighth * 2**3 + seventh * 2**2 + sixth * 2**1 + fifth + fourth * 2**-1 + third * 2**-2 + second * 2**-3 + first * 2**-4

print(f'{decimal}.')