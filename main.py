import random
from hangman_art import stages, logo
from hangman_words import word_list
# from replit import clear


def playmore():
    more = input("Do you want to play again? Enter Y for Yes and N for No: ")
    if more == "Y" or more == "y":
        hangman()
    elif more == "N" or more == "n":
        print("Thank You!!")
    else:
        print("Enter Valid Character")


def hangman():
    score = 120
    print(logo)
    game_is_finished = False
    lives = len(stages) - 1

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)

    display = []
    for _ in range(word_length):
        display += "_"
    print(f' '.join(display))
    while not game_is_finished:
        guess = input("Guess a letter: ").lower()

        # Use the clear() function imported from replit to clear the output between guesses.
        # clear()

        if guess in display:
            print(f"You've already guessed {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life. You Lose 20 points")
            lives -= 1
            score -= 20
            if lives == 0:
                game_is_finished = True
                print(f"You lose. The word is {chosen_word}. Your total score: {score}")
                playmore()

        if not "_" in display:
            game_is_finished = True
            print(f"You win. Score: {score}")
            playmore()

        print(stages[lives])


hangman()

