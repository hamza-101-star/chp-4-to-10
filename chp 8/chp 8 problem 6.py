def make_album(artist, title, num_songs=None):
    album = {
        "artist": artist,
        "title": title
    }
    if num_songs is not None:
        album["songs"] = num_songs
    return album

album1 = make_album("Adele", "30")
album2 = make_album("Coldplay", "Parachutes")
album3 = make_album("Ed Sheeran", "Divide", 12)

print(album1)
print(album2)
print(album3)
