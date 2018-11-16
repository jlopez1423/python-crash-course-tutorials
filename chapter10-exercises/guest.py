filename = 'guest.txt'
guest = input('What in hecks world is your name? ')
with open(filename, 'w') as file_object:
    file_object.write('The persons name is ' + guest)

