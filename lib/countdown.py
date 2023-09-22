# your code goes here!
import time

def countdown(number):
    x = 1
    while x <= number:
        print(f"{number} SECOND(S)!")
        number -= 1
    
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(number):
    x = 1
    while x <= number:
        print(f"{number} SECOND(S)!")
        time.sleep(1)
        number -= 1
    
    print("HAPPY NEW YEAR!")