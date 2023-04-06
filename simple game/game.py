import random

# List of words to choose from
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Select a random word from the list
word = random.choice(words)

# Create a string with underscores for each letter in the word
hidden_word = "_" * len(word)

# Number of tries the user has
max_guesses = 6
remaining_guesses = max_guesses

# Loop until the user guesses the word or runs out of tries
while remaining_guesses > 0 and hidden_word != word:
    print(f"Word: {hidden_word}")
    print(f"Guesses remaining: {remaining_guesses}")
    guess = input("Guess a letter or the whole word: ").lower()
    if guess == word:
        hidden_word = word
    elif guess in word:
        # Replace the corresponding underscores with the guessed letter
        new_hidden_word = ""
        for i in range(len(word)):
            if guess == word[i]:
                new_hidden_word += guess
            else:
                new_hidden_word += hidden_word[i]
        hidden_word = new_hidden_word
    else:
        print("Incorrect guess!")
        remaining_guesses -= 1

# Check if the user won or lost
if hidden_word == word:
    print(f"You guessed the word '{word}'!")
else:
    print(f"You ran out of guesses! The word was '{word}'.")
