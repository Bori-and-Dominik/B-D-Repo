import random
import time


def fishing_game():
    print("Welcome to the Fishing Game!\n")
    print("You have a chance to catch different types of fish.")
    print("Try to catch as many fish as you can within 10 tries!")
    print("Let's start fishing!\n")

    # List of possible fish types
    fish_types = ['Bass', 'Trout', 'Salmon', 'Catfish', 'Piranha']

    # Number of tries the player has
    max_tries = 10
    fish_caught = 0

    # Start the fishing loop
    for attempt in range(1, max_tries + 1):
        print(f"\nAttempt {attempt} of {max_tries}:")

        # Simulate casting the line
        print("Casting the line...")
        time.sleep(1)  # Pause for a moment to simulate the wait

        # Randomly determine if a fish is caught
        catch_chance = random.random()  # Random float between 0 and 1

        if catch_chance < 0.5:  # 50% chance to catch a fish
            # Randomly choose a fish type
            fish = random.choice(fish_types)
            fish_caught += 1
            print(f"You caught a {fish}!")
        else:
            print("No bite this time. Try again!")

    # End of the game
    print(f"\nGame Over! You caught {fish_caught} fish.")

    if fish_caught == 0:
        print("Better luck next time!")
    else:
        print(f"Great job! You caught {fish_caught} fish in {max_tries} attempts!")


# Run the game
fishing_game()
