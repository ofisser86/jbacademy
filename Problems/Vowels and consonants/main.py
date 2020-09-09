vowel = 'aeiou'
while True:
    string = input()
    for i in string:
        if not i.isalpha():
            break

        if i in vowel:
            print('vowel')
        else:
            print("consonant")
    break
