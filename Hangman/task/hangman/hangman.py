import random
# Write your code here
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
print()
pc_word = random.choice(word_list)

guessing_words = ['-' for i in range(len(pc_word))]
wrong_letters = set()
attempts = 0
last_letter = 0
while attempts < 8:
    if '-' not in guessing_words:
        guessing_words[last_letter] = '-'
        print("".join(guessing_words))
        print("You guessed the word!")
        print("You survived!")
        break

    print(''.join(guessing_words))
    letter = input('Input a letter: ').strip(' ')
    if letter in wrong_letters:
        print("You already typed this letter")
        print()
        continue

    if len(letter) != 1:
        print('You should input a single letter')
        print()
        continue
    elif not letter.isascii() or letter.isupper() or not letter.isalpha():
        print('It is not an ASCII lowercase letter')
        print()
        continue

    if letter in pc_word:
        if letter in guessing_words:
            print("You already typed this letter")
            # attempts += 1
            if attempts == 8:
                print("You are hanged!")
                break
            else:
                print()
            continue
        else:
            for j in range(len(pc_word)):
                if pc_word[j] == letter:
                    guessing_words[j] = letter
                    last_letter = j
                    if '-' in guessing_words:
                        print()
    else:
        print("No such letter in the word")
        attempts += 1
        wrong_letters.add(letter)
        if attempts == 8:
            print("You are hanged!")
            break
        else:
            print()
