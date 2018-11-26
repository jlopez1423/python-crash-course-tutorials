filename = 'poll_results.txt'

with open(filename, 'a') as file_object:
    answer = ''
    while(answer != 'q'):
        answer = input("Why are you learning programming? ")
        file_object.write(answer + "\n")

