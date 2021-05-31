

print("Welcome to our survey")
guess = 0

while guess != 25:
    g = input("guess the age of the eldest contestant ")
    guess = int(g)
    if guess == 25:
        print("You win!")
    else:
        if guess > 25:
            print("Too high!")
        else:
            print("Too low!")
print("Game over")