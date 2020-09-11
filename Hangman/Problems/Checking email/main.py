#  and string.rfind('.', (string.rfind('@') - 2)) != -1
def check_email(string):
    if string.count(' ') <= 0 and string.count('@') == 1 and string.find('.', string.index('@') + 2) != -1:
        return True
    return False
