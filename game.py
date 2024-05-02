from guess_handling import *
from main_menu import woddle_word, ALLOWED_GUESSES
from rich.prompt import Prompt
from rich.console import Console
from interaction.db_interaction import database_manager

def play_game(console, woddle_word):
    end_of_game = False
    got_word = False
    already_guessed = []
    full_woddle_pattern = []
    all_words_guessed = []

    while not end_of_game and not got_word:
        guess = Prompt.ask("Please enter your guess").upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You have already guessed this word!\n[/]")
            else:
                console.print("[red]Word must be 5 letters long!\n[/]")
            guess = Prompt.ask("Please enter your guess").upper()
        already_guessed.append(guess)
        guessed, pattern = verify_guess(guess, woddle_word)
        all_words_guessed.append(guessed)
        full_woddle_pattern.append(pattern)


        console.print(*all_words_guessed, sep="\n")
        if guess == woddle_word.upper():
            got_word = True
        if len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    if got_word == True:
        console.print(f"\n[green]Congrats! the correct word was: {woddle_word}[/]")
        console.print(*full_woddle_pattern, sep="\n")
        # database_manager.update_user_wins()
        quit()
    if len(already_guessed) == ALLOWED_GUESSES and guess != woddle_word:
        console.print(f"\n[red]WODDLE X/{ALLOWED_GUESSES}[/]")
        console.print(f'\n[green]Correct Word: {woddle_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
    console.print(*full_woddle_pattern, sep="\n")


