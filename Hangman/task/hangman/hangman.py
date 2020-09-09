import random
# Write your code here
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
print()
pc_word = random.choice(word_list)

guessing_words = ['-' for i in range(len(pc_word))]
attempts = 0
while attempts < 8:
    if '-' not in guessing_words:
        print("".join(guessing_words))
        print("You guessed the word!")
        print("You survived!")
        break

    print(''.join(guessing_words))
    letter = input('Input a letter: ').strip(' ')

    if letter in pc_word:
        if letter in guessing_words:
            print("No improvements")
            attempts += 1
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
        print()
    else:
        print("No such letter in the word")
        attempts += 1
        if attempts == 8:
            print("You are hanged!")
            break
        else:
            print()

