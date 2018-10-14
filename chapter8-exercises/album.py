def make_album(artist_name, album_title, number_of_tracks=''):
    album = {'artist_name': artist_name, 'album_title': album_title}

    if number_of_tracks:
        album['number_of_tracks'] = number_of_tracks

    return album


while True:
    print("\nPress q to quit at any time")
    print("\nPlease enter the album information")

    a_name = input("Please enter the artists name ")
    if a_name == 'q':
        break

    a_title = input("Please enter album title ")
    if a_title == 'q':
        break

    number_of_tracks = input("Please enter the number of tracks ")
    if number_of_tracks == 'q':
        break

    print(make_album(a_name, a_title, number_of_tracks))


# print(make_album('Taylor Swift', 'The album'))
# print(make_album('Eminem', 'Mathew Marshall LP2', 25))
# print(make_album('Dude', 'Some Track'))
