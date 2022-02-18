import random

gnumber = input("Type a number : ")

if gnumber.isdigit():
    gnumber = int(gnumber)
    if gnumber <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,gnumber)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue
    if user_guess == random_number:
        print("You Got It!")     
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in",guesses,"guesses")            
