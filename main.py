import random

def choose_word():
    words = ["apple", "banana", "cherry", "orange", "grape", "pear", "kiwi", "melon"]
    return random.choice(words)

def hangman():
    print("Welcome to Hangman!")
    
    secret_word = choose_word()
    guessed_letters = set()
    attempts_left = 6
    
    while True:
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word to guess: {display_word}")
        print(f"Attempts left: {attempts_left}")
        
        if "_" not in display_word:
            print("Congratulations! You guessed the word.")
            break
        
        if attempts_left == 0:
            print(f"Sorry, you ran out of attempts. The word was '{secret_word}'.")
            break
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess not in secret_word:
            attempts_left -= 1
            print("Incorrect guess.")
        else:
            print("Correct guess!")
    
if __name__ == "__main__":
    hangman()
