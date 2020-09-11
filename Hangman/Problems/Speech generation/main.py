speech_number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_to_speech = input()
for i in numbers_to_speech:
    print(speech_number[int(i)])
