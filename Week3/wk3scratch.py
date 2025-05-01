# Start with this basic structure
music_library = {
    "rock": [
        {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354},
        {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 482}
    ],
    "pop": [
        {"title": "Shape of You", "artist": "Ed Sheeran", "duration": 234},
        {"title": "Blinding Lights", "artist": "The Weeknd", "duration": 201}
    ],
    "hip-hop": [
        {"title": "Lose Yourself", "artist": "Eminem", "duration": 326}
    ]
}

# Task 1: Add a new song to the "rock" genre
# Your code here

music_library['rock'].append({'title':'No sleep til Brooklyn', 'artist': 'The Beastie Boys', 'duration': 188})
print(music_library)


# Task 2: Print all songs in the "pop" genre
# Your code here
print(music_library['pop'])


# Task 3: Calculate the total duration of all songs in "hip-hop"
# Your code heres

total = 0
for song in music_library['hip-hop']:
    total += song['duration']

print(total)  

