import random
R=random.randint(1,100)
print("guess a number between 1 to 100")


x=0
while x==0:
    x=0
    guess=int(input("enter a number u guessed "))
    if guess==R:
        print(f"{guess} is correct guess")
        x=1
    elif guess>R:
        print("Too high")
    else:
        print("Too low")
    