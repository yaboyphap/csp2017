import random

def generate_password():
    i=0
    a = [None] * 9
    for i in range(0,9):
        a[i] = [random.randint(0,9)]
        i += 1
    print a, 'is a suggested password'
    
def test():
    print 'Type in your password to check if it is secure'
    password = str(raw_input('Password: '))
    length = len(password)
    if length < 9:
        print 'Your password is not secure. Must have at least 9 characters!'
        generate_password()
    else:
        print 'Your password is strong'