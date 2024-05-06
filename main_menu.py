from rich.console import Console
from rich.panel import Panel
from rich import print
from sign_up_sign_in import account_manipulation
import game
import interaction.word_api_interaction

class menu:
    def __init__(self, current_user):
        self.USER = current_user
    
ALLOWED_GUESSES = 5


fetch_random_word = interaction.word_api_interaction.word_api_manipulator()
woddle_word = fetch_random_word.get_word()
signed_in = False

if __name__ == '__main__':
    console = Console()
    print(Panel('Welcome to Woddle 🐧', style='bold green', padding=(1,2), title_align='center'))
    
    signed_in = account_manipulation()
    current_user = signed_in.get_response()

    if current_user:
        console.print("[bold green]You may start guessing\n")
        game.play_game(console, woddle_word)