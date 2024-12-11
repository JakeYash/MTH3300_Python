#******************************************************************************
# sprinkler.py
#******************************************************************************
# Name: Jake Yashayev
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
#
# 

x = float(input('Enter width (in ft): '))
y = float(input('Enter length (in ft): '))
sqft = x*y
aIrrigation = sqft*0.8 
#irrigation area is 80% of total

print(f'You have {sqft} square feet of yard area and {aIrrigation} square feet for irrigation.')

rIrrigation = int((aIrrigation/155) + (aIrrigation%155 > 0)) 
#uses the fact that boolean true = 1 and false = 0 to round up 

gpm = 3.11 * rIrrigation
cost = (gpm * 15 * 30) / 748 * 4.49
#15 minutes a day * 30 days a month /748 gallons * $4.49 a gallon

print(f'You will need {rIrrigation} sprinklers in your yard.')

print(f'It will use about {gpm} gallons per minute when running.')

print(f'Your bill will be about ${cost:.2f} per month')
#round to 2 decimal places because money