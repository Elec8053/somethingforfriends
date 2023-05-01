import random

# Set the range of numbers the user can guess from
min_num = 1
max_num = 20

# Generate a random number within the range
secret_number = random.randint(min_num, max_num)

# Set the number of attempts the user has to guess the number
max_guesses = 4

# Keep asking the user for a guess until they run out of guesses or guess the number
for attempt in range(max_guesses):
    # Show the user how many guesses they have left
    print(f"You have {max_guesses - attempt} guesses left.")

    # Ask the user for a guess
    guess = int(input(f"Guess a number between {min_num} and {max_num}: "))

    # Check if the user's guess is correct
    if guess == secret_number:
        print(f"Congratulations, you guessed the number {secret_number}!")
        break
    else:
        # Give the user a hint if their guess is too high or too low
        if guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

# If the user has used all their guesses without guessing the number
else:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")
