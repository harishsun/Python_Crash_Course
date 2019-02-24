def make_album(artist_name, album_title, tracks=''):
    album_details = {'artist': artist_name, 'album': album_title}
    if tracks:
        album_details['tracks'] = tracks
    return album_details

album_info = make_album('mj', 'bad', tracks=7)
print(album_info)