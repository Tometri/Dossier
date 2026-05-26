from functools import reduce
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.55), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]

# Function to pick songs longer than five minutes using the filter function:
def pick_long_songs(songs):
    return list(filter(lambda song: song[1] > 5, songs))
# Get the long songs from the playlist
long_songs = pick_long_songs(playlist)
print("Songs longer than five minutes:")
for song in long_songs:
    print(f"{song[0]} - {song[1]} minutes")

# Using map() to convert all the durations of the songs from minutes to seconds:
def convert_to_seconds(songs):
    return list(map(lambda song: (song[0], song[1] * 60), songs))
# Convert the playlist durations to seconds
playlist_in_seconds = convert_to_seconds(playlist)
print("\nPlaylist with durations in seconds:")
for song in playlist_in_seconds:
    print(f"{song[0]} - {song[1]} seconds")

# Using reduce() to calculate the total duration of the playlist:

def total_duration(songs):
    return reduce(lambda total, song: total + song[1], songs, 0)
# Calculate the total duration of the playlist in minutes
total_duration_minutes = total_duration(playlist)
print(f"\nTotal duration of the playlist: {total_duration_minutes} minutes")