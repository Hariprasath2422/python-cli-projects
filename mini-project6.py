import random

def GuessingGame():
    rand_num = random.randint(1, 100)
    print("Guess the number between 1 and 100!")
    print("You have 6 attempts to guess the correct answer.")
    
    for i in range(1, 7):  # Loop 6 times for 6 attempts
        attempt = int(input(f"Attempt {i}/6: Enter your guess: "))
        
        if attempt < rand_num:
            print("Too low!")
        elif attempt > rand_num:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {i} attempts!")
            break
    else:
        print(f"Sorry, you didn't guess the number. The correct number was {rand_num}.")

# Call the function to start the game
GuessingGame()

    