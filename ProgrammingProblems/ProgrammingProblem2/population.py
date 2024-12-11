#******************************************************************************
# invest.py
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
# import math for e
#
# 
# 
import math

#ask for initial numbers
pop = int(input('Enter initial population: '))
timePeriod = float(input('Enter first time period (in years): '))
growthRate = float(input('Enter first growth rate (in percent): '))

#calculate first population number
pop = pop * math.e ** (growthRate * .01 * timePeriod)

timePeriod = float(input('Enter second time period (in years): '))
growthRate = float(input('Enter second growth rate (in percent): '))

#repeat
pop = pop * math.e ** (growthRate * .01 * timePeriod)

timePeriod = float(input('Enter third time period (in years): '))
growthRate = float(input('Enter third growth rate (in percent): '))

pop = pop * math.e ** (growthRate * .01 * timePeriod)


print('The final population is', pop)