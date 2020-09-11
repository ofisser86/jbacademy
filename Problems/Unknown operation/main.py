# TODO: Do it later do not give up!

def solve():
    # Write your code here
    if hidden_operation('and'):
        if hidden_operation('and'):
            print('and')
            print(hidden_operation('and'))
        elif not hidden_operation('and'):
            print('and')
            print(hidden_operation('and'))
        else:
            print('not')
    elif hidden_operation('or'):
        if hidden_operation('or'):
            print('or')
            print(hidden_operation('or'))
        if not hidden_operation('or'):
            print('or')
            print(hidden_operation('or'))
        else:
            print('not')
    else:
        print('not')