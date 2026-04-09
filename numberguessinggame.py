import random

DIFFICULTY_LEVELS = {
    "1": ("Easy",   1, 50),
    "2": ("Medium", 1, 100),
    "3": ("Hard",   1, 200),
}

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    for key, (name, low, high) in DIFFICULTY_LEVELS.items():
        print(f"  {key}. {name} (1 - {high})")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in DIFFICULTY_LEVELS:
            name, low, high = DIFFICULTY_LEVELS[choice]
            print(f"\n[{name}] Guess a number between {low} and {high}.")
            return low, high
        print("Invalid choice. Please enter 1, 2, or 3.")


def play_round(low, high):
    secret = random.randint(low, high)
    attempts = 0

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        if guess < low or guess > high:
            print(f"Please guess a number between {low} and {high}.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! Try higher.")
        elif guess > secret:
            print("Too high! Try lower.")
        else:
            print(f"Correct! You guessed {secret} in {attempts} attempt{'s' if attempts != 1 else ''}.")
            return attempts


def main():
    print("=" * 45)
    print("       Welcome to the Number Guessing Game!")
    print("=" * 45)

    best_score = None

    while True:
        low, high = choose_difficulty()
        attempts = play_round(low, high)

        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"New best score: {best_score} attempt{'s' if best_score != 1 else ''}!")
        else:
            print(f"Your best score so far: {best_score} attempt{'s' if best_score != 1 else ''}.")

        again = input("\nPlay again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print(f"\nThanks for playing! Final best score: {best_score} attempt{'s' if best_score != 1 else ''}. Goodbye!")
            break


if __name__ == "__main__":
    main()
