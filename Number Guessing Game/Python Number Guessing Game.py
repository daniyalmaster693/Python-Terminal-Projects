import random, string, time

name = input ("Hello, What is your name?")
print ("Hello," + name)
time.sleep (0.8)
print ("Are you ready to guess this number?")
time.sleep (0.5)
answer = input ("Enter yes or no:")

if answer == "yes":
    print ("The game is starting...")
elif answer == "no":
    print ("-__-")

print ("Picking a number...")
time.sleep (0.5)

print ("The number is between 1-1000")
time.sleep (0.5)

print ("You will have 10 attempts to guess this number")
time.sleep (0.5)

print ("3....")
time.sleep (0.5)

print ("2...")
time.sleep (0.5)

print ("1..")
time.sleep (0.7)

print ("Go!")

number = random.randrange (1,1000)
guess = int(input("Enter any number:"))
while number == guess:
    if guess < number:
        print ("Too low")
    elif guess > number:
        print ("Too high")
    else:
     break 

print ("Congratutlations! You guessed the number correctly!")

time.sleep (0.5)

print ("Would you like to play again?")
time.sleep (0.5)

print ("Enter yes or no:")
time.sleep (0.5)




