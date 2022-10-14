import prompt
import brain_games.games.brain_prime
import brain_games.games.brain_calc
import brain_games.games.brain_even
import brain_games.games.brain_gcd
import brain_games.games.brain_progression


# Game rules dictionary
rules = {
    'brain-even': 'Answer "yes" if the number is even, otherwise answer "no".',
    'brain-gcd': 'Find the greatest common divisor of given numbers.',
    'brain-calc': 'What is the result of the expression?',
    'brain-progression': 'What number is missing in the progression?',
    'brain-prime':
        'Answer "yes" if given number is prime. Otherwise answer "no".',
}

# Dictionary with game round generating functions
rounds = {
    'brain-even': brain_games.games.brain_even.generate_round,
    'brain-gcd': brain_games.games.brain_gcd.generate_round,
    'brain-calc': brain_games.games.brain_calc.generate_round,
    'brain-progression': brain_games.games.brain_progression.generate_round,
    'brain-prime': brain_games.games.brain_prime.generate_round
}


def game_engine(game):
    """Greet user. Print rules.
    Ask question 3 times. Compare answer with user guess,
    if answer is correct, then ask again.
    If answer is incorrect game is over.
    """

    # Greet user
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')

    # Print rules
    print(f'{rules[game]}')

    # What game would be playing
    get_round = rounds[game]

    index = 0
    while index < 3:

        # Get game round
        question, answer = get_round()

        # Ask user a question
        print(f'Question: {question}')

        # Prompt user for a guess
        guess = input('Your answer: ').strip()

        # Copmare user guess and answer
        if answer == guess:
            print('Correct!')
            index += 1
        else:
            print(f"'{guess}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{answer}'.")
            print(f'Let\'s try again, {name}!')
            break

    # User gave 3 correct answer
    if index == 3:
        print(f'Congratulations, {name}!')


def main():
    game = 'brain-prime'
    game_engine(game)


if __name__ == '__main__':
    main()
