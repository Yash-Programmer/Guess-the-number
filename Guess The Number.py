import random
import playsound
import time

Name = input("What Your Name is:  ")
print("Well " + Name + ''', Lets Play the guess number game''')

Instructions = input("Would You Like me to read out the instruction:  ")

if Instructions.lower() == "yes":
    print("OK", Name + ',')
    print('\n        Instructions: -')
    time.sleep(2)
    print("             : This is a Guess the Number Game.")
    time.sleep(2)
    print("             : Here you have to guess the number between 0-20.")
    time.sleep(2)
    print("             : You Have to just Write Your Guess.")
    time.sleep(2)
    print("             : You will get 6 chances for this.")
    time.sleep(2)
    print(
        "             : If Your Guess will be higher or lower than the number to guess. Python will say,'Your Guess is Too High' or 'Your Guess is Too low'")
    time.sleep(2)
    print("             : These are all the information you need to know.\n")
    time.sleep(2)
    print("Now, Let's Start\n")
elif Instructions.lower() == 'no':
    print("No Issues", Name,'\n')
else:
    print("Invalid")

Secret_Number = random.randint(1, 20)

time.sleep(2)

for i in range(1, 7):
    Guess = int(input("Take a Guess:  "))
    if Guess < Secret_Number:
        print("Your Guess is Too low")
    elif Guess > Secret_Number:
        print("Your Guess is too High")
    else:
        break

if Guess == Secret_Number:
    print("You Won!! The Number is", Secret_Number, 'You Answered Correctly in', i)
    playsound.playsound('Guess The Number Game (Sound)/Win.mp3')
else:
    playsound.playsound('Guess The Number Game (Sound)/Lose.mp3')
    print("\n Nope! The Number I was thinking is", Secret_Number, "You didn't get it right in", i)
    print('You Lost')
exit()
