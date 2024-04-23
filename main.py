from rich.console import console
import integrate_wordapi
import make_guess

def correct_place(letter):
    return f'[black on green]{letter}[/]'
def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'
def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'

fetch_random_word = integrate_wordapi.word_api_manipulator()
woodle_word = fetch_random_word.get_word()
guess.user_guess(woodle_word, guess=0)

