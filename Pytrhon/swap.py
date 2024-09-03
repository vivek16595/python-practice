import random

user_inputt= "Enter the number: "
num = int(input(user_inputt))

if num == random.randint(1,5) :
    print("Congratulation You Won")
else:
    print("You Lose")