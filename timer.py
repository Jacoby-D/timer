#Import Modules
import time
import math

#Define function "countdown"
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        
    print('Times Up!')
 
#Take input for length of timer in seconds
t = input('Enter the time in seconds: ')

#Run function
countdown(int(t))
