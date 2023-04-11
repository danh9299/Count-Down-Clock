# We need the following libaries:
    # playsound: The playsound helps us play the sound when time reaches 0
    # time: The time.sleep() helps us keep the program waiting 1s before printing the time every second
    # os: The os.system("cls") allows us to clear the screen in the terminal
from playsound import playsound
import time
import os
# Define a function count_down() that counts the time down
    # The paramater for this function is the time we want to count down (in seconds)
def countDown(countDownTime):
    elapsedTime = 0
    os.system("cls")
    while elapsedTime < countDownTime:

        # Wait for 1 second before printing
        time.sleep(1)

        # For each loop, the time passes by 1 second
        elapsedTime += 1

        # timeLeft is in seconds
        timeLeft = countDownTime - elapsedTime
        
        # The integral part of the timeLeft shows the remaining minutes
        minuteLeft = timeLeft//60

        # The fractional part of the timeLeft shows the remaining seconds
        secondLeft = timeLeft%60

        # Show the count down
            #The :02d means 2 digits with a 0 in front of the number
        os.system("cls")
        print("Time left:",f"{minuteLeft:02d}:{secondLeft:02d}")
    # The loop ends when the timeLeft is 0, that's when the sound plays
    playsound("count_down_sound.mp3")

# Main
# Input the minute
minu = "a"
while minu.isdigit() == False:
    try:
        minu = int(input("Enter the minutes to count down: "))
    except:
        print("Sometime went wrong, please try again!")
    minu = str(minu)
minu = int(minu)

# Input the second
seco = "a"
while seco.isdigit() == False:
    try:
        seco = int(input("Enter the seconds to count down: "))
    except:
        print("Sometime went wrong, please try again!")
    seco = str(seco)
seco = int(seco)

# Count the total countDownTime
countDownTime = minu*60 + seco

# Run the count down
countDown(countDownTime)


