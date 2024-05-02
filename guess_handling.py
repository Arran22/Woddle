SQUARES = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect_letter(letter):
    return f'[white]{letter}[/]'

def verify_guess(guess, woddle_word):
    woddle_word = woddle_word.upper()
    guessed = []
    woddle_pattern = []
    for index, letter in enumerate(guess, 0):
        if woddle_word[index] == letter:
            guessed += correct_place(letter)
            woddle_pattern.append(SQUARES['correct_place'])
        elif (letter in woddle_word):
            guessed += correct_letter(letter)
            woddle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            woddle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(woddle_pattern)