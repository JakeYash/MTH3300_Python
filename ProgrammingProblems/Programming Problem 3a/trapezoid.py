#******************************************************************************
# trapezoid.py
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
#i didn't use the formula, as although it makes sense, it was easier to wrap my
#head around calculating each trapezoid, which also let me factor out the 1/2
#and was more in line with what i would do on paper in calc
#This also works for reversed bounds


import math

#function, 1/ln(x)
def f_x(x):
    return (1/math.log(x))

#ask for the bounds and automatically cast as proper types

a = float(input("Enter the lower bound: "))

b = float(input("Enter the upper bound: "))

n = int(input("Enter the number of trapezoids: "))

#formula for delta x
delta_x = (b-a)/n


#total is the counter

total = 0

#this is base1 + base2 in a loop for the amount of trapezoids there are
#the first and last base will only occur once each with every other occuring
#twice, just like the formula
#delta x is being incremented by the amount of trapezoids there are for each step
for i in range(n):
    total += f_x(a + (i * delta_x)) + f_x(a + ((i+1) * delta_x))
    
#must multiply by delta x but also divide by 2 beause the 1/2 from
#b1+b2/2 was factored out
answer = delta_x/2 * total



#f string to round to 8 decimal places (said 10 in pdf but gradescope 8)
print(f'The definite integral is approximately: {answer:.8f}')



#this is an alternate solution using the formula
#total = (f_x(a) + f_x(b))/2
#or i in range(1,n):
#   total += f_x(a + (i * delta_x))
#
#answer = delta_x * total