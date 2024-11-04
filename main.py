import sys
import random


def ask_question(guess):
    answer = input(
        f'Is it {guess}? (Answer with "greater", "less", or "yes"): ').strip().lower()
    return answer


def computer_guesses():
    low = 1
    high = 100
    step = 0

    while True:
        step += 1
        guess = (low + high) // 2
        answer = ask_question(guess)

        if answer == 'greater':
            low = guess + 1
        elif answer == 'less':
            high = guess - 1
        elif answer == 'yes':
            print(f'Perfect! The computer guessed it in {step} steps!')
            return step
        else:
            print('Please answer with "greater", "less", or "yes".')


def computer_guesses_random():
    low = 1
    high = 100
    step = 0

    while low <= high:
        step += 1
        guess = random.randint(low, high)
        answer = ask_question(guess)

        if answer == 'greater':
            low = guess + 1
        elif answer == 'less':
            high = guess - 1
        elif answer == 'yes':
            print(f'Perfect! The computer guessed it in {step} steps!')
            return step
        else:
            print('Please answer with "greater", "less", or "yes".')


def user_guesses():
    number = random.randint(1, 100)
    steps = 0

    while True:
        try:
            guess = int(input("Your guess: "))
            steps += 1

            if guess == number:
                print(f'Correct! You guessed it in {steps} steps.')
                return steps
            elif guess < number:
                print("greater")
            else:
                print("less")
        except ValueError:
            print("Please enter a valid number.")


def test_algorithms(num_trials=10):
    print("Testing computer guessing algorithms...\n")

    print("Using: computer Search Algorithm")
    for _ in range(num_trials):
        steps = computer_guesses()
        print(f"Got the correct answer in {steps} steps\n")

    print("\nUsing: Random Choice Algorithm")
    for _ in range(num_trials):
        steps = computer_guesses_random()
        print(f"Got the correct answer in {steps} steps\n")


def exit_game():
    print("Exiting the game. Goodbye!")
    sys.exit()


def play_rounds(num_rounds):
    user_wins = 0
    computer_wins = 0

    for round_number in range(1, num_rounds + 1):
        print(f"\nRound {round_number}!")
        print("Computer is guessing your number.")
        steps_computer = computer_guesses()

        print("\nNow it's your turn to guess the computer's number.")
        steps_user = user_guesses()

        if steps_computer < steps_user:
            print("Computer wins this round!")
            computer_wins += 1
        elif steps_user < steps_computer:
            print("You win this round!")
            user_wins += 1
        else:
            print("It's a tie for this round!")

    print(f"\nFinal Score: You - {user_wins}, Computer - {computer_wins}")


def main_menu():
    print("Welcome to the Guessing Game!")

    while True:
        print("\nChoose a game mode:")
        print("1 - Computer guesses your number (Computer Search)")
        print("2 - Computer guesses your number (Random Choice)")
        print("3 - You guess the computer's number")
        print("4 - Test algorithms")
        print("5 - Play rounds")
        print("Type 'exit' to quit the game")

        choice = input("Enter your choice: ").lower()

        if choice == '1':
            computer_guesses()
        elif choice == '2':
            computer_guesses_random()
        elif choice == '3':
            user_guesses()
        elif choice == '4':
            test_algorithms()
        elif choice == '5':
            rounds = input(
                "How many rounds would you like to play? (default is 3): ")
            num_rounds = int(rounds) if rounds.isdigit() else 3
            play_rounds(num_rounds)
        elif choice == 'exit':
            exit_game()
        else:
            print("Error choice. Try again.")


main_menu()
