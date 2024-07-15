import random

# List of words for the game
word_list = ["python", "hangman", "challenge", "programming", "random", "example"]

# Function to select a random word
def get_random_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the hangman game
def play_hangman():
    word = get_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            incorrect_guesses += 1

        current_state = display_word(word, guessed_letters)
        print(current_state)

        if "_" not in current_state:
            print("Congratulations! You've guessed the word.")
            break

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game Over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
