favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite langague is " +
              favorite_languages[name].title() + "!")

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + ".")
#
# # Looping through all the keys in a dictionary
# for name in favorite_languages.keys():
#     print(name.title())

