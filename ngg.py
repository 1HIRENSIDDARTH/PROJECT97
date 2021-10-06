import random
number = random.randint(1,9)
chances=0

print("number guessing game")
print("guess a number between 1-9")

while chances < 5:

    guess = int(input("Enter your guess:- "))

    if guess == number:
        print("Congratulations!! YOU WIN ")
        break

    elif guess < number:
          print("Your guess was too low Guess a number higher ", guess)

    else:
         print("Your guess was too high: Guess a number lower than", guess)

    if not chances < 5:
         print()
         print("YOU LOSE !!! The number is ", number)




