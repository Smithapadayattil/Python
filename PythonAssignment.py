#number guessing game
import random

result=random.randint(1,50)
print(result)
guess=int(input("Enter a number between 1 and 50:"))
if guess>result:
    print("Your number is high")
elif guess<result:
    print("Your number is  low")
else:
    print("You won!")