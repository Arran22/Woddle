def user_guess(woodle_word, guess):
    if (guess+1)<5:
        print("Guess number", (guess+1), ":")
        guess += 1
        make_guess()
    else:
        print("Mission failed, word was:" & woodle_word)

def make_guess():
    print("making guess...")