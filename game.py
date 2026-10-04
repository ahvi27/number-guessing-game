import random


DIFFICULTIES = {
    "1": (1, 10, 5, "Easy"),
    "2": (1, 50, 7, "Medium"),
    "3": (1, 100, 10, "Hard"),
}


def get_difficulty() -> tuple[int, int, int, str]:
    """Ask the player to select a valid difficulty level."""
    while True:
        print("\nChoose difficulty:")
        print("1. Easy   (1–10, 5 attempts)")
        print("2. Medium (1–50, 7 attempts)")
        print("3. Hard   (1–100, 10 attempts)")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Invalid choice. Please enter 1, 2, or 3.")


def get_guess(low: int, high: int) -> int:
    """Return a valid whole-number guess within the permitted range."""
    while True:
        value = input(f"Enter your guess ({low}–{high}): ").strip()
        try:
            guess = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if low <= guess <= high:
            return guess
        print(f"Your number must be between {low} and {high}.")


def play_round() -> bool:
    """Play one round and return True when the player wins."""
    low, high, max_attempts, level = get_difficulty()
    secret = random.randint(low, high)

    print(f"\n{level} level: I selected a number from {low} to {high}.")
    print(f"You have {max_attempts} attempts. Good luck!")

    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}")
        guess = get_guess(low, high)

        if guess == secret:
            print(f"Correct! You guessed {secret} in {attempt} attempt(s). 🎉")
            return True
        if guess < secret:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

        remaining = max_attempts - attempt
        if remaining:
            print(f"Attempts remaining: {remaining}")

    print(f"\nGame over! The correct number was {secret}.")
    return False


def wants_to_replay() -> bool:
    """Ask whether the player wants another round."""
    while True:
        answer = input("\nPlay again? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please enter y or n.")


def main() -> None:
    print("=" * 38)
    print("      NUMBER GUESSING GAME")
    print("=" * 38)

    rounds = 0
    wins = 0
    while True:
        rounds += 1
        if play_round():
            wins += 1
        if not wants_to_replay():
            break

    print(f"\nThanks for playing! You won {wins} of {rounds} round(s).")


if __name__ == "__main__":
    main()
