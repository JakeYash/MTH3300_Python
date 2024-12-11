#******************************************************************************
# newton.py
#******************************************************************************
# Name: Jake Yashayev
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# NONE
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
# I made a function to create polynomials with the list index indicating the exp
# This allowed for the derive function and eval function using the same framework
# We infinitely do the Newton's method until the answer is within the threshhold
# and break at that point
# FIRST, WRITE CODE TO GET INPUT FOR THE COEFFICIENTS BELOW, starting with x^0 
# see the pdf specifications for the exact input prompts and formatting

#function to get the list of coefficients, n = number of terms
def getCoList(n):
    co_list = []
    for i in range(n):
        x = float(input(f'Enter x^{i} coefficient: '))
        co_list.append(x)
    return co_list

#function to derive a function using coefficients, using the power rule
#the power of each element in the list is indicated by its position
def getDerivList(co_list):
    deriv_list = []
    for i in range(len(co_list)-1):
        deriv_list.append(co_list[i+1] * (i + 1))
    return deriv_list
  
#go through each element, adding its value to a total, using an x value to the 
#power of the position of the coefficient, multiplied by the coefficient
def evalList(co_list,x):
    answer = 0
    for i in range(len(co_list)):
        answer += co_list[i] * x ** i
    return answer

#the initial list representing the funciton, its just the coefficients,
#activated to actual yield values by the functions that evaluate
og_list = getCoList(6)

#******************************************************************************
guess = float(input('Enter guess: ')) # the initial guess for Newton's method
    
# the number of iterations for Newton'n method
threshold = float(input('Enter threshold for approximation: '))
#******************************************************************************

# INSERT CODE FOR NEWTON'S METHOD BELOW

#get deriv of list
deriv_list = getDerivList(og_list)
guessCount = 0

#infinite loop until break point hit
while True:
    #get the value of the original function using the most recent guess
    current_guess_result = evalList(og_list, guess)
    
    #if the result isnt within zero by the threshhold, you exit the loop
    if abs(current_guess_result) <= threshold:
        break
    
    #now make the next x-value guess
    guess = guess - current_guess_result/(evalList(deriv_list,guess))
    guessCount += 1


print(guess)
print(f"It took {guessCount} iterations")

