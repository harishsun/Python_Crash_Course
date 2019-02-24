def make_album(artist_name, album_title):
    album_details = {'artist': artist_name, 'album': album_title}
    return album_details

album_info = make_album('mj', 'bad')
print(album_info)