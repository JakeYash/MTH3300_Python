##******************************************************************************
# trapezoid.py
#******************************************************************************
# Name: 
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
#
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#

import math

#DEFINE YOUR FUNCTION f HERE:
def f(x):
    return (1 + (math.sin(x))**2) ** 0.5  
    
    


#TEST CODE FOR THE FUNCTION f: (uncomment to test, comment out when submitting)
#print(f(0.2), '(this should equal 1.0195437719875284 if your function works)')
#print(f(-1.4), '(this should equal 1.4039626670016296 if your function works)')


#CODE FOR GETTING THE INPUT:
A = float(input('Enter the lower bound: '))
B = float(input('Enter the upper bound: '))
N = int(input('Enter the number of trapezoids: '))


#INSERT CODE FOR COMPUTING APPROXIMATION OF DEFINITE INTEGRAL USING TRAPEZOIDAL RULE HERE:
################################################
sum = 0
delta_x = (B-A)/N

for i in range(N+1):
    if i == 0 or i == N:
        sum += f(A + i*delta_x)
    else:
        sum += 2*f(A + i*delta_x)

integral = (delta_x)/2 * sum        
    








################################################

#CODE FOR PRINTING THE APPROXIMATION TO 8 DECIMAL PLACES, integral is the variable for the approximation 
print(f'The definite integral is approximiately: {integral:.8f}')