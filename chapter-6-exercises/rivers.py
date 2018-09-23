rivers = {
    'nile': 'egypt',
    'salinas': 'usa',
    'lerma': 'mexico'
}

for river in rivers:
    print("The " + river.title() + ' runs through ' + rivers[river])

# name of each river in the dictionary
for river in rivers:
    print(river)

for river in rivers.values():
    print(river)