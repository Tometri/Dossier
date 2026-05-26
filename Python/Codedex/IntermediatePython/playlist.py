liked_songs = {
    'Heavy Metal' : 'Juice WRLD',
    'Contained' : 'Juice WRLD',
    'USD' : 'Juice WRLD',
    'Red Moonlight' : 'Juice WRLD',
    'Righteous' : 'Juice WRLD',
    'Sometimes' : 'Juice WRLD',
    'Lucid Dreams' : 'Juice WRLD',
    'Tonight' : 'Juice WRLD',
    'Die Homes' : 'G Fredo',
    'Pros' : 'City Morgue',
    'HaHa Waco' : 'City Morgue',
    '33rd Blakk Glass' : 'City Morgue',
    'Nitro Cell' : 'City Morgue',
    'Chinatown' : 'Polo G',
    'Go Stupid' : 'Polo G',
    'Flex' : 'Polo G',

}

def write_liked_songs(liked_songs, file_name):
    with open(file_name, 'w') as file:
        for song, artist in liked_songs.items():
            file.write(f"{song} by {artist}\n")

write_liked_songs(liked_songs, 'liked_songs.txt')
