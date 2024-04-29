from rich.console import Console
from rich.panel import Panel
from rich import print
import game
import interaction.word_api_interaction

class menu:
    def __init__(self, current_user):
        self.USER = current_user
    
    # # WELCOME_MESSAGE -= f'\n[black on green] Welcome to Woddle 🐧 [/]\n'
    # PLAYER_INSTRUCTIONS = "You may start guessing\n"
ALLOWED_GUESSES = 5


fetch_random_word = interaction.word_api_interaction.word_api_manipulator()
woddle_word = fetch_random_word.get_word()

if __name__ == '__main__':
    console = Console()
    print(Panel('Welcome to Woddle 🐧', style='bold green', padding=(1,2), title_align='center'))
    # console.print(f'\n[black on green] Welcome to Woddle 🐧 [/]\n')
    console.print("[bold green]You may start guessing\n")
    game.play_game(console, woddle_word)