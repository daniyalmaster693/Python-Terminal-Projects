import random, time

print ("Would you like to roll the dices?")

answer = input ("Enter yes or no:")

if answer == "yes":
    print ("The dices are rolling")
elif answer == "no":
    print ("-__-")

time.sleep (0.5)

min_value = 1
max_value = 12

roll_again = "yes"

while roll_again == "yes":
    print ("Rolling the dices...")
    time.sleep (0.5)
    print ("The values are...")
    time.sleep (0.7)

    value1 = random.randint(min_value, max_value)
    value2 = random.randint(min_value, max_value)
    print (value1, value2)
    roll_again = input ("Press 'yes' to roll the dices again.")

print ("Have a good day")