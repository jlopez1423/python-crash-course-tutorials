filename = 'guestbook.txt'

with open(filename, 'a') as file_object:
    status = ''

    while (status != 'n'):
        name = input('What is your name?')
        file_object.write('Persons name is: ' + name + '\n')
        status = input("Would you like to continue?")

