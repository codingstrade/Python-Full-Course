import random
while True:
    secret_number = random.randint(1,10)

    guess = int(input("Guess a number between 1 to 10: "))

    if guess == secret_number:
        print("Congrats, you have the secret number!")
        break
    elif guess < secret_number:
        print("Your guess is too low, try again. the number was:", secret_number)
    else:
        print("your guess is too high, try again. the number was:", secret_number)