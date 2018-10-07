age = ''
while age != 'q':
    age = input('What is your age? ')
    if age == 'q':
        break
    elif int(age) < 3:
        print('You get a free ticket')
    elif 3 <= int(age) <= 12:
        print('Your ticket is $10')
    elif int(age) >= 12:
        print('Your Your ticket is $15')
