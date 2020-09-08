import random
# Write your code here
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
pc_word = random.choice(word_list)
word = input(f'Guess the word {pc_word[:3]}' + '-' * len(pc_word[3:]) + ': > ')
if word == pc_word:
    print("You survived!")
else:
    print("You are hanged!")
