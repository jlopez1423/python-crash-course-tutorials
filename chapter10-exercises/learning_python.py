filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    test = line.replace('learned', 'c')
    print(test.rstrip())
