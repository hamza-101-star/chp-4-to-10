def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if num_songs is not None:
        album["songs"] = num_songs
    return album

print("Enter album information. Type 'quit' at any time to exit.")

while True:
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'quit':
        break

    title = input("Enter the album title: ")
    if title.lower() == 'quit':
        break

    num_songs_input = input("Enter the number of songs (or press Enter to skip): ")
    if num_songs_input.lower() == 'quit':
        break

    if num_songs_input:
        album = make_album(artist, title, int(num_songs_input))
    else:
        album = make_album(artist, title)

    print("Album created:", album)
    print()
