def show_magicians(magician_names):
    for magician_name in magician_names:
        print(magician_name.title())


def make_great(magician_names):
    result = []

    for magician_name in magician_names:
        result.append(magician_name + ' the great')

    return result


magician_names = ['alice', 'malice', 'balice', 'walice']
great_magicians = make_great(magician_names[:])

show_magicians(great_magicians)