favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# list of people who should take the fave lang poll.
people = ['jose', 'sarah', 'ginger', 'edward', 'bob', 'bill']

for person in people:
    if person in favorite_languages.keys():
        print(person.title() + " thank you for taking our poll!")