#Question #4
def star(n):
    x = n//2 #midpoint, very useful
    #outer loop traverses rows
    for i in range(n):
        #inner loop traverses columns
        for j in range(n):
            #if we are in the first half of rows before the midpoint
            if(i < x):
                #print stars from 1/4 to 3/4, essentially that middle section
                if (n//4 < j <= (n//4+x)):
                    print('*', end ='')
                #otherwise print spaces
                else:
                    print(' ', end = '')
            #if we are in the middle row, its just all stars
            elif (i== n//2):
                print('*', end = '')
            #confusing part (for me at least):
            #this is the pattern for how the start column and end column of the 
            #stars in the bottom half are. They slide one to the left and right
            #respectively with each iteration
            elif ((i-x-1) < j <= (x + (n-i-1))):
                print('*', end = '')
            #if they arent in between those columns spaces should fill up
            else:
                print(' ',end = '')
        #new line at the end of every row
        print()