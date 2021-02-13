import random
import string
from Dictionary import words


if __name__ == '__main__':
    def get_valid_word(words):
        word = random.choice(words)
        while '-' in word or ' ' in word:
            get_valid_word(words)
        return word.upper()


    def hangman():
        word = get_valid_word(words)
        word_letter = set(word)
        alphabets = set(string.ascii_uppercase)
        used_letters = set()
        lives = 10

        while len(word_letter) > 0 and lives > 0:
            print('The letters you have used are:',' '.join(used_letters))
            print(f'Lives left: {lives}')

            word_output = [letter if letter in used_letters else '_' for letter in word]

            print(' '.join(word_output))
            user_input = input('Guess a Letter:').upper()
            if user_input in alphabets - used_letters:
                used_letters.add(user_input)
                if user_input in word_letter:
                    word_letter.remove(user_input)
                else:
                    lives = lives -1
            elif user_input in used_letters:
                print(f'You have already used {user_input}.')
            else:
                print(f'{user_input} is not a valid alphabet.')
        if(lives > 0):
            print(f'Congratulations! The word is {word}')
        else:
            print(f'Sorry you lost! The word is {word}')





hangman()