import random
chaos = random.randrange(1,101)
if chaos == 69:
    print("Nice!")
guess = int(input("Enter your guess:"))
print("guess:",guess)
print(guess)
while True:
    if guess == chaos:
        print("Correct!")
        break
    if guess < chaos:
        print("Larger")
    if guess > chaos:
        print("Smaller")
    guess = int(input("Try Again!:"))