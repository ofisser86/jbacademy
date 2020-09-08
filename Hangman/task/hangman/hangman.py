import random
# Write your code here
word_list = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N")
print()
pc_word = random.choice(word_list)

guessing_words = ['-' for i in range(len(pc_word))]
for i in range(8):
    print(''.join(guessing_words))
    letter = input('Input a letter:').strip(' ')
    if letter in pc_word:
        for j in range(len(pc_word)):
            if pc_word[j] == letter:
                guessing_words[j] = letter
        print()
    else:
        print("No such letter in the word")
        print()

print("""
Thanks for playing!
We'll see how well you did in the next stage
""")
